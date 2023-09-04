<template>
  <div class="PoliticsInfo">
    <Head :title="data.title" :isshow="isshow" :name="back"></Head>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <!-- 时间选择器 -->
        <div class="selectTime">
          <!-- <div>
            <span
              v-show="timeSum>0&&timeSum<60"
              style="color:rgba(255,255,255,0.68);display:inline-block;margin-right:10px"
            >({{timeSum}}s)</span>
            <el-date-picker
              v-model="timevalue"
              type="daterange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              @change="getDateValue()"
            ></el-date-picker>
          </div>-->
        </div>
        <div class="groupBox">
          <div class="gropTop">
            <div class="mesBase common">
              <Icon></Icon>
              <p class="title">事件基本属性</p>
              <div class="mesBaseBox">
                <div class="baseMes">
                  <table>
                    <tr>
                      <td class="td1" valign="top">关键词：</td>
                      <td class="td2" valign="top">
                        <ul class="news">
                          <li
                            class="every_news"
                            v-for="(item, index) in keyWordList"
                            :key="index"
                          >
                            <p>{{ item }}</p>
                          </li>
                        </ul>
                      </td>
                      <td class="td3" valign="top">
                        <div class="goleft">
                          <div class="leave">
                            <div class="effect">
                              <div v-if="data.grade == 1">
                                <img src="../../assets/img/danger1.png" alt />
                                <span style="color: #741b33">一级</span>
                              </div>
                              <div v-if="data.grade == 2">
                                <img src="../../assets/img/danger2.png" alt />
                                <span style="color: #773f3b">二级</span>
                              </div>
                              <div v-if="data.grade == 3">
                                <img src="../../assets/img/danger3.png" alt />
                                <span style="color: #7b8744">三级</span>
                              </div>
                              <div v-if="data.grade == 4">
                                <img src="../../assets/img/danger4.png" alt />
                                <span style="color: #b7f2f9">四级</span>
                              </div>
                              <div v-if="data.grade == 5">
                                <img src="../../assets/img/danger5.png" alt />
                                <span style="color: #e6ccff">五级</span>
                              </div>
                            </div>
                            <div class="per_box">
                              <p>影响力指标</p>
                              <div class="perbox">
                                <div
                                  class="per"
                                  :style="
                                    'width:' + data.impactIndicators + '%'
                                  "
                                ></div>
                              </div>
                              <p>{{ data.impactIndicators }}</p>
                            </div>
                          </div>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td class="td1" valign="top">标签：</td>
                      <td class="td2" colspan="2" valign="top">
                        <ul class="lables">
                          <li
                            class="every_lable"
                            v-for="(item, index) in labelWordList"
                            :key="index"
                          >
                            <p>{{ item }}</p>
                          </li>
                        </ul>
                      </td>
                    </tr>
                  </table>
                </div>
                <p class="content">{{ data.detailsynopsis }}</p>
              </div>
            </div>
            <div class="mesPredicted common">
              <Icon></Icon>
              <div class="mesPredicted_box">
                <p class="title" style="margin: 0.3125rem 0 0.3125rem">
                  事件发生地
                </p>
                <div id="myChartMap"></div>
              </div>
            </div>
          </div>
          <div class="gropBottom common">
            <Icon></Icon>
            <div style="display: flex; width: 100%; height: 100%">
              <div class="relation">
                <div class="select_local">
                  <div>
                    <el-select v-model="value" placeholder="请选择">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.label"
                      ></el-option>
                    </el-select>
                  </div>
                </div>
                <div
                  id="myChartActive"
                  class="myCharts"
                  :style="{ width: '100%', height: '80%' }"
                ></div>
              </div>
              <div class="select_event">
                <ul>
                  <li @click="clickOne(1)" v-show="flag">
                    <div
                      class="colorset"
                      :style="
                        one
                          ? 'background-color:#fb6237'
                          : 'background-color:#834635'
                      "
                    ></div>
                    <p>自媒体热度</p>
                  </li>
                  <li @click="clickOne(2)" v-show="flag">
                    <div
                      class="colorset"
                      :style="
                        two
                          ? 'background-color:#07d9eb'
                          : 'background-color:#217c76'
                      "
                    ></div>
                    <p>自媒体参与</p>
                  </li>
                  <li @click="clickOne(3)" v-show="!flag">
                    <div
                      class="colorset"
                      :style="
                        three
                          ? 'background-color:#827ee4'
                          : 'background-color:#53517a'
                      "
                    ></div>
                    <p>情感倾向</p>
                  </li>
                  <li @click="clickOne(4)" v-show="!flag">
                    <div
                      class="colorset"
                      :style="
                        four
                          ? 'background-color:#f2123c'
                          : 'background-color:#7f2637'
                      "
                    ></div>
                    <p>用户活跃度</p>
                  </li>
                </ul>
                <div
                  id="myChartZhe"
                  class="myChartZhe"
                  :style="{ width: '100%', height: '100%' }"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "../../../static/js/chinamap/china.js";
import Head from "../../components/Head/Head.vue";
import Icon from "../../components/Icon/Icon.vue";
import BMap from "BMap";
var vm;
var timer;
export default {
  name: "Group",
  components: {
    Head,
    Icon,
  },
  data() {
    return {
      isshow: true,
      timeSum: 60,
      timevalue: ["2020-01-03", "2020-01-03"],
      options: [],
      value: "",
      back: "返回",
      one: false,
      two: true,
      three: true,
      four: true,
      linecolor: "#fb6237",
      data: "",
      keyWordList: [],
      labelWordList: [],
      mapDate: {},
      // 自媒体热度
      selfMediaPopularity: {
        actual: [],
        predicted: [],
      },
      // 自媒体参与度
      selfMediaParticipation: {
        actual: [],
        predicted: [],
      },
      // 情感倾向
      emotional: {
        actual: [],
        predicted: [],
      },
      // 用户活跃度
      liveness: {
        actual: [],
        predicted: [],
      },
      //折线图横坐标的值
      xDate: [],
      xActual: [],
      xPredicted: [],
      chartZhe: "",
      option: [],
      // 关系图数据
      currentRelation: [],
      node: [],
      relation: [],
      categories: [],
      optionActive: {},
      chart1: "",
      flag: true,
    };
  },
  watch: {
    value(newValue, oldValue) {
      if (newValue != oldValue) {
        this.upDateRela();
      }
    },
  },
  created() {
    this.data = JSON.parse(this.$route.query.item);
    // 关键词列表
    this.keyWordList = this.data.keyWord.split(",");
    this.labelWordList = this.data.labelWord.split(",");

    this.mapDate = {
      name: this.data.title,
      value: [this.data.longitude, this.data.latitude, this.data.number],
    };

    let dateBox = this.data.relation[0].effectList;
    for (let i = 0; i < dateBox.length; i++) {
      console.log(dateBox[i]);
      this.xDate.push(dateBox[i].dateTime);

      // // 自媒体热度
      this.selfMediaPopularity.actual.push(dateBox[i].selfMediaPopularity[0]);
      this.selfMediaPopularity.predicted.push(
        dateBox[i].selfMediaPopularity[1]
      );
      // 自媒体参与度
      this.selfMediaParticipation.actual.push(
        dateBox[i].selfMediaParticipation[0]
      );
      this.selfMediaParticipation.predicted.push(
        dateBox[i].selfMediaParticipation[1]
      );
      // 情感倾向
      this.emotional.actual.push(dateBox[i].emotional[0]);
      this.emotional.predicted.push(dateBox[i].emotional[1]);
      // 用户活跃度
      this.liveness.actual.push(dateBox[i].liveness[0]);
      this.liveness.predicted.push(dateBox[i].liveness[1]);
    }
    this.flag = true;
    this.xActual = this.selfMediaPopularity.actual;
    this.xPredicted = this.selfMediaPopularity.predicted;

    // 关系图数据集合
    this.currentRelation = this.data.relation;
    // 获得下拉框数据

    for (let i = 0; i < this.currentRelation.length; i++) {
      let obj = {
        label: this.currentRelation[i].name,
        value: this.currentRelation[i].value,
      };
      this.options.push(obj);
    }
    this.value = this.options[0].label;
  },
  mounted() {
    this.drowlineZhe();
    this.drowBaiduMap();
  },
  destroyed() {},
  methods: {
    // 绘制地图
    drowBaiduMap() {
      var map = new BMap.Map("myChartMap"); // 创建Map实例
      var point = new BMap.Point(this.data.longitude, this.data.latitude);
      map.centerAndZoom(point, 12);
      var marker = new BMap.Marker(point); // 创建标注
      map.addOverlay(marker); // 将标注添加到地图中
      marker.disableDragging(); // 不可拖拽
      marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
      map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
    },
    // 重置关系图数据

    upDateRela() {
      this.zheDate(this.value);
      // 改变关系图数据
      this.node = [];
      this.relation = [];
      this.categories = [];
      this.optionActive = {};
      this.chart1 = "";
      for (let i = 0; i < this.currentRelation.length; i++) {
        if (this.value == this.currentRelation[i].name) {
          // 重置关系图数据
          let node = this.currentRelation[i].relationDetail.node;
          let relation = this.currentRelation[i].relationDetail.relation;
          for (let j = 0; j < node.length; j++) {
            let obj = {
              name: node[j].name,
              symbolSize: node[j].symbolSize / 3,
              category: node[j].category,
              itemStyle: {
                color: "#827EE4",
              },
            };
            this.node.push(obj);
          }
          for (let j = 0; j < relation.length; j++) {
            let obj = {
              source: relation[j].source,
              target: relation[j].target,
              label: {
                show: false,
              },
            };
            this.relation.push(obj);
          }

          this.categories = this.currentRelation[i].relationDetail.categories;
        }
      }
      console.log("数据更新了");
      this.drowlineActive();
    },

    // 折线图数据处理
    zheDate(e) {
      console.log(44444444444444, e);

      for (let i = 0; i < this.currentRelation.length; i++) {
        if (this.value == this.currentRelation[i].name) {
          this.xDate = [];
          this.xActual = [];
          this.xPredicted = [];
          // 自媒体热度
          this.selfMediaPopularity = {
            actual: [],
            predicted: [],
          };
          // 自媒体参与度
          this.selfMediaParticipation = {
            actual: [],
            predicted: [],
          };
          // 情感倾向
          this.emotional = {
            actual: [],
            predicted: [],
          };
          // 用户活跃度
          this.liveness = {
            actual: [],
            predicted: [],
          };
          let dateBox = this.currentRelation[i].effectList;
          for (let j = 0; j < dateBox.length; j++) {
            console.log(dateBox[j]);
            this.xDate.push(dateBox[j].dateTime);
            // // 自媒体热度
            this.selfMediaPopularity.actual.push(
              dateBox[j].selfMediaPopularity[0]
            );
            this.selfMediaPopularity.predicted.push(
              dateBox[j].selfMediaPopularity[1]
            );
            // 自媒体参与度
            this.selfMediaParticipation.actual.push(
              dateBox[j].selfMediaParticipation[0]
            );
            this.selfMediaParticipation.predicted.push(
              dateBox[j].selfMediaParticipation[1]
            );
            // 情感倾向
            this.emotional.actual.push(dateBox[j].emotional[0]);
            this.emotional.predicted.push(dateBox[j].emotional[1]);
            // 用户活跃度
            this.liveness.actual.push(dateBox[j].liveness[0]);
            this.liveness.predicted.push(dateBox[j].liveness[1]);
          }

          if (this.currentRelation[i].type == 1) {
            this.flag = true;
            this.clickOne(1);
          } else if (this.currentRelation[i].type == 2) {
            this.flag = false;
            this.clickOne(3);
          }
        }
      }
      // 折线图数据处理
    },

    //实例化折线图
    drowlineZhe() {
      this.chartZhe = this.$echarts.init(document.getElementById("myChartZhe"));
      this.option = {
        xAxis: {
          type: "category",
          data: this.xDate,
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: "#ffffff",
            },
          },
          axisTick: {
            show: false,
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed",
            },
          },
        },
        yAxis: {
          type: "value",
          min: 0,
          max: 160,
          interval: 20,
          axisLine: {
            lineStyle: {
              color: "#ffffff",
            },
          },
          splitLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
        },
        dataZoom: [
          {
            start: 0,
          },
          {
            type: "slider",
            backgroundColor: "#09275D",
            fillerColor: "#09275D",
            borderColor: "#09275D",
          },
        ],
        series: [
          {
            data: this.xActual,
            type: "line",
            lineStyle: {
              color: this.linecolor,
              width: 1,
            },
            symbolSize: 0,
          },
          {
            data: this.xPredicted,
            type: "line",
            lineStyle: {
              color: this.linecolor,
              width: 1,
              type: "dashed",
            },
            symbolSize: 0,
          },
        ],
      };
      this.chartZhe.clear();
      this.chartZhe.setOption(this.option);
    },
    // 点击切换折线图数据
    clickOne(e) {
      if (e == 1) {
        this.one = false;
        this.two = true;
        this.three = true;
        this.four = true;
        this.linecolor = "#fb6237";
        this.xActual = this.selfMediaPopularity.actual;
        this.xPredicted = this.selfMediaPopularity.predicted;
      } else if (e == 2) {
        this.one = true;
        this.two = false;
        this.three = true;
        this.four = true;
        this.linecolor = "#07e9db";
        this.xActual = this.selfMediaParticipation.actual;
        this.xPredicted = this.selfMediaParticipation.predicted;
      } else if (e == 3) {
        this.one = true;
        this.two = true;
        this.three = false;
        this.four = true;
        this.linecolor = "#827ee4";
        this.xActual = this.emotional.actual;
        this.xPredicted = this.emotional.predicted;
      } else {
        this.one = true;
        this.two = true;
        this.three = true;
        this.four = false;
        this.linecolor = "#f2123c";
        this.xActual = this.liveness.actual;
        this.xPredicted = this.liveness.predicted;
      }
      console.log(this.xDate, this.xActual, this.xPredicted);

      this.drowlineZhe();
    },
    //实例化关系图
    drowlineActive() {
      this.chart1 = this.$echarts.init(
        document.getElementById("myChartActive")
      );
      this.optionActive = {
        backgroundColor: "transparent", // 背景颜色
        tooltip: {
          // 提示框的配置
          formatter: function (param) {
            return param.data.nameDetail;
          },
        },

        series: [
          {
            type: "graph", // 系列类型:关系图
            top: "10%", // 图表距离容器顶部的距离
            roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。[ default: false ]
            force: {
              // 力引导布局相关的配置项，力引导布局是模拟弹簧电荷模型在每两个节点之间添加一个斥力，每条边的两个节点之间添加一个引力，每次迭代节点会在各个斥力和引力的作用下移动位置，多次迭代后节点会静止在一个受力平衡的位置，达到整个模型的能量最小化。
              // 力引导布局的结果有良好的对称性和局部聚合性，也比较美观。
              repulsion: 150, // [ default: 50 ]节点之间的斥力因子(关系对象之间的距离)。支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
              edgeLength: [50, 20], // [ default: 30 ]边的两个节点之间的距离(关系对象连接线两端对象的距离,会根据关系对象值得大小来判断距离的大小)，
              // 这个距离也会受 repulsion。支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长。如下示例:
              // 值最大的边长度会趋向于 10，值最小的边长度会趋向于 50      edgeLength: [10, 50]
            },
            // layout: "circular", // 图的布局。[ default: 'none' ]
            layout: "force", // 图的布局。[ default: 'none' ]

            symbol: "circle",
            lineStyle: {
              // 关系边的公用线条样式。其中 lineStyle.color 支持设置为'source'或者'target'特殊值，此时边会自动取源节点或目标节点的颜色作为自己的颜色。
              normal: {
                // color: "target", // 线的颜色[ default: '#aaa' ]
                width: 2, // 线宽[ default: 1 ]
                type: "solid", // 线的类型[ default: solid ]   'dashed'    'dotted'
                opacity: 0.5, // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。[ default: 0.5 ]
                curveness: 0.2, // 边的曲度，支持从 0 到 1 的值，值越大曲度越大。[ default: 0 ]
              },
            },
            label: {
              // 关系对象上的标签
              normal: {
                show: true, // 是否显示标签
                position: "bottom", // 标签位置:'top''left''right''bottom''inside''insideLeft''insideRight''insideTop''insideBottom''insideTopLeft''insideBottomLeft''insideTopRight''insideBottomRight'
                textStyle: {
                  // 文本样式
                  fontSize: 12,
                },
              },
            },
            edgeLabel: {
              // 连接两个关系对象的线上的标签
              normal: {
                show: true,
                textStyle: {
                  fontSize: 11,
                },
                formatter: function (param) {
                  // 标签内容
                  return param.data.category;
                },
              },
            },
            data: this.node,
            links: this.relation,
            category: this.categories,
            //  data: [{
            //     name: 'node01',
            //     des: 'nodedes01',
            //     symbolSize: 20,
            //     category: 0,
            // }, {
            //     name: 'node02',
            //     des: 'nodedes02',
            //     symbolSize:20,
            //     category: 1,
            // }, {
            //     name: 'node03',
            //     des: 'nodedes3',
            //     symbolSize: 20,
            //     category: 1,
            // }, {
            //     name: 'node04',
            //     des: 'nodedes04',
            //     symbolSize: 20,
            //     category: 1,
            // }, {
            //     name: 'node05',
            //     des: 'nodedes05',
            //     symbolSize: 20,
            //     category: 1,
            // }],
            // links: [{
            //     source: 'node01',
            //     target: 'node02',
            //     name: 'link01',
            //     des: 'link01des'
            // }, {
            //     source: 'node01',
            //     target: 'node03',
            //     name: 'link02',
            //     des: 'link02des'
            // }, {
            //     source: 'node01',
            //     target: 'node04',
            //     name: 'link03',
            //     des: 'link03des'
            // }, {
            //     source: 'node01',
            //     target: 'node05',
            //     name: 'link04',
            //     des: 'link05des'
            // }],
            // categories: [{'name':1},{'name':2}],
          },
        ],
        animationEasingUpdate: "quinticInOut", // 数据更新动画的缓动效果。[ default: cubicOut ]    "quinticInOut"
        animationDurationUpdate: 100, // 数据更新动画的时长。[ default: 300 ]
      };
      this.chart1.clear();
      this.chart1.setOption(this.optionActive);
    },
  },
};
</script>


<style scoped lang="less">
@import url("./Group.less");
/deep/ .el-input {
  input {
    background: transparent;
    border: 1px solid #fff;
    color: #fff;
    padding: 0;
    padding-left: 0.625rem;
    border-radius: 0;
  }
}
/deep/ .el-range-editor--small.el-input__inner {
  background: transparent;
  border: none;
  color: #fff;
  padding: 0;
}
/deep/ .el-date-editor .el-range-input {
  background: transparent;
  border: none;
  color: #fff;
  padding: 0;
}
/deep/ .el-range-separator {
  margin-top: 6px !important;
  color: #fff !important;
}
/deep/ .myCharts input {
  font-size: 9px !important;
}
/deep/ .el-date-editor .el-range-input {
  width: 5.625rem;
}
.el-range-editor--small.el-input__inner {
  width: 15rem;
}
</style>
