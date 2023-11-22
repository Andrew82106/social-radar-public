<template>
  <div class="PoliticsInfo">
    <Head :title="data.title" :isshow="isshow" :name="back"></Head>
    <div class="cover" v-if="coverVisible">
      <i class="el-icon-close cover-icon" @click="handleCoverClose"></i>
      <div
        class="common"
        style="width: 100%; height: 100%; padding: 10px"
        v-if="eventClick"
      >
        <Icon></Icon>
        <div class="time-line cover-time__line">
          <div class="timeline-content">
            <div
              class="time-line-div"
              v-for="(item, index) in data.forwardList"
              :key="index"
            >
              <div class="content_detail">
                <div
                  v-for="(item, index) in item.data"
                  :key="index"
                  class="content_detail--item"
                >
                  <div class="back_item_titel" style="text-align: center">
                    {{ item.type }}
                  </div>
                  <div class="back_item_content">
                    <ul>
                      <li v-for="(ite, idx) in item.nameList" :key="idx">
                        {{ ite }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <div ref="circular">
                <div class="circle"></div>
              </div>
              <div>{{ item.createTime }}</div>
              <div class="img-dotted" ref="dotted"></div>
            </div>
          </div>
        </div>
        <div style="width: 100%; height: 50%">
          <p class="title" style="color: #fff">
            {{ chartTitleMap[chartType] }}
          </p>
          <div class="select_event">
            <div
              v-if="chartType === 'subComment' || chartType === 'subArticle'"
            >
              <ul>
                <li @click="handleChartChange('subComment')">
                  <div
                    class="colorset"
                    :style="
                      chartType === 'subComment'
                        ? 'background-color:#fb6237'
                        : 'background-color:#834635'
                    "
                  ></div>
                  <p style="color: #fff">评论量</p>
                </li>
                <li @click="handleChartChange('subArticle')">
                  <div
                    class="colorset"
                    :style="
                      chartType === 'subArticle'
                        ? 'background-color:#07d9eb'
                        : 'background-color:#217c76'
                    "
                  ></div>
                  <p style="color: #fff">发文量</p>
                </li>
              </ul>
            </div>
            <div
              id="coverLineChart"
              class="myChartZhe"
              :style="{ width: '100%', height: '80%' }"
            ></div>
          </div>
        </div>
      </div>
      <div
        class="chartarea common"
        style="width: 100%; height: 100%"
        v-else-if="graphClick"
      >
        <Icon></Icon>
        <div
          id="coverGraph"
          class="myCharts"
          :style="{ width: '100%', height: '100%' }"
        ></div>
      </div>
    </div>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <div class="groupBox">
          <div class="gropTop">
            <div class="mesBase common">
              <Icon></Icon>
              <p class="title">信息基本属性</p>
              <div class="mesBaseBox">
                <div class="baseMes">
                  <table>
                    <tr>
                      <!-- <td class="td1" valign="top">信息熵：</td>
                      <td class="td2" valign="top">{{data.informationEntropy}}</td> -->
                      <td class="td1" valign="top"></td>
                      <td class="td2" valign="top"></td>
                      <td rowspan="2" class="td3" valign="top">
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
                              <p>{{ data.impactIndicators }}%</p>
                            </div>
                          </div>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td class="td1" valign="top">关键词：</td>
                      <td class="td2" style="padding-top: 0" valign="top">
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
            <div class="mesPredicted common" style="display: flex; width: 49%">
              <Icon></Icon>
              <ul class="imglist" style="width: 25%; overflow-y: auto">
                <li class="imgItem">
                  <img src="../../assets/img/1.png" alt="" />
                </li>
                <li class="imgItem">
                  <img src="../../assets/img/2.png" alt="" />
                </li>
                <li class="imgItem">
                  <img src="../../assets/img/3.png" alt="" />
                </li>
                <li class="imgItem">
                  <img src="../../assets/img/4.jpg" alt="" />
                </li>
              </ul>
              <video controls>
                <source src="../../assets/media/test3.mp4" type="video/mp4" />

                Sorry, your browser doesn't support embedded videos.
              </video>
            </div>
          </div>
          <div class="gropBottom">
            <div
              class="chartarea common"
              style="width: 49%; height: 100%; overflow: hidden"
              @click="showGraph"
            >
              <Icon @icon-click="showGraph"></Icon>
              <div
                id="myChartActive"
                class="myCharts"
                :style="{ width: '100%', height: '100%', margin: '5px 0' }"
              ></div>
            </div>
            <div
              class="eventLine common"
              style="width: 49%; height: 100%"
              @click="showChart"
            >
              <Icon></Icon>
              <div class="time-line">
                <div class="timeline-content">
                  <div
                    class="time-line-div"
                    style="overflow: hidden; padding-right: 40px"
                    v-for="(item, index) in data.forwardList"
                    :key="index"
                  >
                    <div class="content_detail">
                      <div
                        v-for="(item, index) in item.data"
                        :key="index"
                        class="content_detail--item"
                      >
                        <div class="back_item_titel" style="text-align: center">
                          {{ item.type }}
                        </div>
                        <div class="back_item_content">
                          <ul>
                            <li v-for="(ite, idx) in item.nameList" :key="idx">
                              {{ ite }}
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                    <div ref="circular">
                      <div class="circle"></div>
                    </div>
                    <div>{{ item.createTime }}</div>
                    <div class="img-dotted" ref="dotted"></div>
                  </div>
                </div>
              </div>
              <div class="timeline-chart">
                <p class="title">{{ chartTitleMap[chartType] }}</p>
                <div class="select_event">
                  <div
                    v-if="
                      chartType === 'subComment' || chartType === 'subArticle'
                    "
                  >
                    <ul>
                      <li @click="handleChartChange('subComment')">
                        <div
                          class="colorset"
                          :style="
                            chartType === 'subComment'
                              ? 'background-color:#fb6237'
                              : 'background-color:#834635'
                          "
                        ></div>
                        <p>评论量</p>
                      </li>
                      <li @click="handleChartChange('subArticle')">
                        <div
                          class="colorset"
                          :style="
                            chartType === 'subArticle'
                              ? 'background-color:#07d9eb'
                              : 'background-color:#217c76'
                          "
                        ></div>
                        <p>发文量</p>
                      </li>
                    </ul>
                  </div>
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
  </div>
</template>

<script>
import "../../../static/js/chinamap/china.js";
import Head from "../../components/Head/Head.vue";
import Icon from "../../components/Icon/Icon.vue";
import effectList from "../../untils/effectList.js";

var vm;
const subCommentData = {
  date: ["2020-01-03", "2020-01-04", "2020-01-05", "2020-01-06", "2020-01-08"],
  actual: [23, 68, 35, 43, 15],
  predicted: [19, 76, 31, 41, 18],
};
const subArticleData = {
  date: ["2020-01-03", "2020-01-04", "2020-01-05", "2020-01-06", "2020-01-08"],
  actual: [68, 94, 137, 87, 53],
  predicted: [79, 81, 140, 95, 41],
};
const groupArticleData = {
  date: [
    "2020/09/13 9:07",
    "2020/09/13 15:29",
    "2020/09/13 20:10",
    "2020/09/14 11:47",
    "2020/09/14 23:21",
    "2020/09/15 7:34",
    "2020/09/16 18:49",
    "2020/09/18 12:36",
  ],
  actual: [275, 354, 412, 323, 252],
  data: [5904, 7914, 42842, 43160, 46703, 48969, 51327, 52649],
  predicted: [294, 342, 431, 312, 267],
};
export default {
  name: "policyAnalyze",
  components: {
    Head,
    Icon,
  },
  data() {
    return {
      title: "涉政信息分析系统", //页面标题
      timeSum: 60,
      // timevalue: ["2020-01-03", "2020-01-03"],
      subCommentData,
      subArticleData,
      groupArticleData,
      linecolor: "",
      isshow: true,
      coverVisible: false,
      eventClick: false,
      graphClick: false,
      back: "返回",
      data: {},
      keyWordList: [],
      labelWordList: [],
      chartType: "groupArticle",
      chartTitleMap: {
        subComment: "订阅号评论量预测",
        subArticle: "订阅号发文量预测",
        groupArticle: "受众群体数量",
      },
      //折线图横坐标的值
      xDate: [],
      xActual: [],
      xPredicted: [],
      chartZhe: "",
      option: [],
      effectList: [],
      flag: true,
      webId: "",
    };
  },
  created() {
    this.data = JSON.parse(this.$route.query.item);
    this.keyWordList = this.data.keyWord.split(",");
    this.labelWordList = this.data.labelWord.split(",");
    this.effectList = effectList.data.resultList;
  },
  mounted() {
    this.drowlineZhe();
    this.drowlineActive("myChartActive");
  },
  destroyed() {},
  methods: {
    handleCoverClose() {
      this.coverVisible = false;
      this.graphClick = false;
      this.eventClick = false;
      this.chartType = "groupArticle";
      this.drowlineZhe();
    },
    showGraph() {
      this.coverVisible = true;
      this.graphClick = true;
      setTimeout(() => {
        this.drowlineActive("coverGraph", 30, 200, 600, {
          right: 25,
          top: 25,
          itemGap: 20,
          itemHeight: 30,
        });
      });
    },
    showChart() {
      this.coverVisible = true;
      this.eventClick = true;
      setTimeout(() => {
        this.drowlineZhe();
      });
    },
    //折线图
    drowlineZhe() {
      const chartDataMap = {
        subComment: this.subCommentData,
        subArticle: this.subArticleData,
        groupArticle: this.groupArticleData,
      };
      const _this = this;
      this.xDate = chartDataMap[this.chartType].date;
      // this.xActual = chartDataMap[this.chartType].actual;
      this.xPredicted = chartDataMap[this.chartType].predicted;
      this.xActual = chartDataMap[this.chartType].data;
      const id = this.coverVisible ? "coverLineChart" : "myChartZhe";
      const chart = this.$echarts.init(document.getElementById(id));
      const data = [
        {
          name: "2019/9/13 09:07",
          value: ["2019/9/13 09:07", 5904],
        },
        {
          name: "2019/9/13 15:29",
          value: ["2019/9/13 15:29", 7914],
        },
        {
          name: "2019/9/13 20:10",
          value: ["2019/9/13 20:10", 42842],
        },
        {
          name: "2019/9/14 11:47",
          value: ["2019/9/14 11:47", 45160],
        },
        {
          name: "2019/9/14 23:21",
          value: ["2019/9/14 23:21", 54703],
        },
        {
          name: "2019/9/15 07:34",
          value: ["2019/9/15 07:34", 57969],
        },
        {
          name: "2019/9/16 18:49",
          value: ["2019/9/16 18:49", 60327],
        },
        {
          name: "2019/9/18 12:36",
          value: ["2019/9/18 12:36", 63649],
        },
      ];
      const predictdata = [
        {
          name: "2019/9/13 09:07",
          value: ["2019/9/13 09:07", 5904],
        },
        {
          name: "2019/9/13 15:29",
          value: ["2019/9/13 15:29", 15121],
        },
        {
          name: "2019/9/13 20:00",
          value: ["2019/9/13 20:00", 28432],
        },
        {
          name: "2019/9/14 08:00",
          value: ["2019/9/14 08:00", 50654],
        },
        {
          name: "2019/9/14 20:00",
          value: ["2019/9/14 20:00", 56585],
        },
        {
          name: "2019/9/15 08:00",
          value: ["2019/9/15 08:00", 62612],
        },
        {
          name: "2019/9/15 20:00",
          value: ["2019/9/15 20:00", 65123],
        },
        {
          name: "2019/9/16 08:00",
          value: ["2019/9/16 08:00", 68003],
        },
        {
          name: "2019/9/16 20:00",
          value: ["2019/9/16 20:00", 70101],
        },
        {
          name: "2019/9/17 08:00",
          value: ["2019/9/17 08:00", 72454],
        },
        {
          name: "2019/9/17 20:00",
          value: ["2019/9/17 20:00", 74600],
        },
        {
          name: "2019/9/18 08:00",
          value: ["2019/9/18 08:00", 76750],
        },
        {
          name: "2019/9/18 12:36",
          value: ["2019/9/18 12:36", 77900],
        },
      ];
      var anchor = [
        { name: "2019/09/13 00:00:00", value: ["2019/09/13 00:00:00", 0] },
        { name: "2019/09/14 00:00:00", value: ["2019/09/14 00:00:00", 43379] },
        { name: "2019/09/15 00:00:00", value: ["2019/09/15 00:00:00", 52907] },
        { name: "2019/09/16 00:00:00", value: ["2019/09/16 00:00:00", 59148] },
        { name: "2019/09/17 00:00:00", value: ["2019/09/17 00:00:00", 59583] },
        { name: "2019/09/18 00:00:00", value: ["2019/09/18 00:00:00", 62661] },
        { name: "2019/09/18 00:00:00", value: ["2019/09/19 00:00:00"] },
      ];
      const option = {
        tooltip: {
          trigger: "axis",
          formatter: function (params) {
            const title = params[0].value[0] + "<br>";
            let content = "";
            params.forEach((param) => {
              const cur = `${param.marker}${param.seriesName}: ${param.value[1]} <br>`;
              content += cur;
            });
            return title + content;
          },
        },
        xAxis: {
          type: "time",
          // interval: 3600,
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: "#ffffff",
            },
          },
          axisTick: {
            show: false,
          },
          axisLabel: { interval: 0 },
          splitLine: {
            show: false,
            lineStyle: {
              type: "dashed",
            },
          },
        },
        yAxis: {
          type: "value",
          min: 5000,
          show: this.coverVisible,
          // max:
          //   this.chartType === "groupArticle"
          //     ? 500
          //     : Math.max.apply(this, this.xActual.concat(this.xPredicted)),
          // interval: this.chartType === "groupArticle" ? 50 : 20,
          interval: 10000,
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
        // dataZoom: [
        //   {
        //     start: 0,
        //   },
        //   {
        //     type: "slider",
        //     backgroundColor: "#09275D",
        //     fillerColor: "#09275D",
        //     borderColor: "#09275D",
        //   },
        // ],
        legend: {
          data: ["实际数量", "预测数量"],
          textStyle: {
            color: "#fff",
          },
        },
        series: [
          {
            data,
            name: "实际数量",
            type: "line",
            lineStyle: {
              color: "rgba(224, 106, 72, 1)",
              width: 2,
            },
            symbolSize: 5,
          },
          {
            data: predictdata,
            type: "line",
            name: "预测数量",
            lineStyle: {
              color: "#7a6b7e",
              width: 2,
              type: "dashed",
            },
            symbolSize: 5,
          },
        ],
      };
      chart.clear();
      chart.setOption(option);
    },
    handleChartChange(type) {
      this.chartType = type;
      //折线图横坐标的值
      this.xDate = [];
      this.xActual = [];
      this.xPredicted = [];
      this.drowlineZhe();
    },
    drowlineActive(
      id,
      symbolSize = 15,
      edgeLength,
      repulsion,
      legendStyle = { right: 15, top: 5, itemGap: 13, itemHeight: 20 }
    ) {
      const chart = this.$echarts.init(document.getElementById(id));
      const categories = [
        {
          name: "一级订阅号",
          symbol: "image://./static/graph-icon/isub.jpg",
          label: {
            color: "red",
          },
        },
        {
          name: "二级订阅号",
          symbol: "image://./static/graph-icon/usub.jpg",
          label: {
            color: "#426c96",
          },
        },
        {
          name: "订阅号",
          symbol: "image://./static/graph-icon/usub.jpg",
          label: {
            color: "#426c96",
          },
        },
        {
          name: "一级群组",
          symbol: "image://./static/graph-icon/igroup.jpg",
          label: {
            color: "red",
          },
        },
        {
          name: "二级群组",
          symbol: "image://./static/graph-icon/ugroup.jpg",
          label: {
            color: "#426c96",
          },
        },
        {
          name: "群组",
          symbol: "image://./static/graph-icon/ugroup.jpg",
          label: {
            color: "#426c96",
          },
        },
        {
          name: "一级用户",
          symbol: "image://./static/graph-icon/iuser.jpg",
          label: {
            color: "red",
          },
        },
        {
          name: "二级用户",
          symbol: "image://./static/graph-icon/uuser.jpg",
          label: {
            color: "#426c96",
          },
        },
        {
          name: "用户",
          symbol: "image://./static/graph-icon/uuser.jpg",
          label: {
            color: "#426c96",
          },
        },
      ];
      const option = {
        // backgroundColor: "transparent", // 背景颜色
        tooltip: {
          // 提示框的配置
          formatter: function (param) {
            return param.data.des;
          },
        },
        legend: [
          {
            // selectedMode: 'single',
            ...legendStyle,
            type: "scroll",
            orient: "vertical",
            textStyle: {
              color: "#426c96",
            },
            pageTextStyle: {
              color: "#fff",
            },
            data: [
              {
                name: "订阅号",
                icon: "image://./static/graph-icon/usub.jpg",
              },
              {
                name: "群组",
                icon: "image://./static/graph-icon/ugroup.jpg",
              },
              {
                name: "用户",
                icon: "image://./static/graph-icon/uuser.jpg",
              },
            ],
          },
        ],
        series: [
          {
            type: "graph", // 系列类型:关系图
            top: "10%", // 图表距离容器顶部的距离
            left: 0,
            draggable: true,
            roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            // focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。[ default: false ]
            force: {
              // 力引导布局相关的配置项，力引导布局是模拟弹簧电荷模型在每两个节点之间添加一个斥力，每条边的两个节点之间添加一个引力，每次迭代节点会在各个斥力和引力的作用下移动位置，多次迭代后节点会静止在一个受力平衡的位置，达到整个模型的能量最小化。
              // 力引导布局的结果有良好的对称性和局部聚合性，也比较美观。
              repulsion: repulsion ? repulsion : 150, // [ default: 50 ]节点之间的斥力因子(关系对象之间的距离)。支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
              edgeLength: edgeLength ? edgeLength : [50, 20], // [ default: 30 ]边的两个节点之间的距离(关系对象连接线两端对象的距离,会根据关系对象值得大小来判断距离的大小)，
              // 这个距离也会受 repulsion。支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长。如下示例:
              // 值最大的边长度会趋向于 10，值最小的边长度会趋向于 50      edgeLength: [10, 50]
            },
            // layout: "circular", // 图的布局。[ default: 'none' ]
            layout: "force", // 图的布局。[ default: 'none' ]

            symbol: "circle",
            symbolSize: symbolSize,
            cursor: "pointer",
            lineStyle: {
              // 关系边的公用线条样式。其中 lineStyle.color 支持设置为'source'或者'target'特殊值，此时边会自动取源节点或目标节点的颜色作为自己的颜色。
              normal: {
                // color: "target", // 线的颜色[ default: '#aaa' ]
                width: 2, // 线宽[ default: 1 ]
                type: "solid", // 线的类型[ default: solid ]   'dashed'    'dotted'
                opacity: 0.5, // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。[ default: 0.5 ]
                curveness: 0, // 边的曲度，支持从 0 到 1 的值，值越大曲度越大。[ default: 0 ]
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
            // edgeLabel: {
            //   // 连接两个关系对象的线上的标签
            //   normal: {
            //     show: true,
            //     textStyle: {
            //       fontSize: 11,
            //     },
            //     formatter: function (param) {
            //       // 标签内容
            //       return param.data.category;
            //     },
            //   },
            // },
            data: [
              {
                name: "望野 Visionary",
                des: "订阅人数 : <br>2358<br>重点账号 : <br>夏沫<br>夏雨荷",
                category: 2,
              },
              {
                name: "習近平和牠的姘頭們",
                des:
                  "订阅人数 : <br>620<br>重点账号 : <br>Armstrong<br>秦蒋玮斑",
                category: 1,
              },
              {
                name: "燧人氏@askedif", // 账户
                category: 8,
              },
              {
                name: "中共政治局主持习近平",
                des:
                  "群成员数 : <br>196<br>重点账号 : <br>燧人氏@askedif<br>先谈分蛋糕 再谈做蛋糕@renminwansui",
                category: 4,
              },
              {
                name: "Vegeta@Lone857857", // 账户
                category: 7,
              },
              {
                name: "习近平@wswindows7", // 账户
                category: 8,
              },
              {
                name: "庆丰末年那些事儿",
                des:
                  "订阅人数 : <br>211<br>重点账号 : <br>差不多得了先生<br>Winnie TheFlu",
                category: 0,
              },
              {
                name: "长安街日报",
                des:
                  "订阅人数 : <br>3339<br>重点账号 : <br>CaptchatBot<br>天推-- 黑哥",
                category: 1,
              },
              {
                name: "CCP病毒 武汉疫情交流群",
                des:
                  "群成员数 : <br>1646<br>重点账号 : <br>燧人氏@askedif<br>众归",
                category: 5,
              },
              {
                name: "法外之地",
                des:
                  "群成员数 : <br>185<br>重点账号 : <br>李春姬@scarlett_butler24<br>MonaYan@monawyuymm",
                category: 3,
              },
              {
                name: "萌豚中央通讯社（Mengtun News）",
                des:
                  "订阅人数 : <br>1322<br>重点账号 : <br>境外势力马克思<br>FEE MAC",
                category: 2,
              },
              {
                name: "辱包群",
                des:
                  "群成员数 : <br>38<br>重点账号 : <br>TADASHI SAKAI @viqkhn<br>Paku KimuGon @pakukimugon",
                category: 5,
              },
              {
                name: "郭 大神@xidabi", // 账户
                category: 7,
              },
              {
                name: "习主席治国理念学习讨论小组",
                des: "群成员数 : <br>77<br>重点账号 : <br>郭 大神@xidabi",
                category: 4,
              },
              {
                name: "Panzer faust @SiegeofPython", // 账户
                category: 7,
              },
              {
                name: "FBI【共狗殺手】@opop1298",
                category: 7,
              },
              {
                name: "Iee ann @wangchao123234",
                category: 8,
              },
              {
                name: "乳透社",
                des:
                  "订阅人数 : <br>5904<br>重点账号 : <br>梁家河扛麦熊<br>新津天皇 孙笑川",
                category: 0,
              },
              {
                name: "噫~这世界",
                des: "订阅人数 : <br>9369<br>重点账号 : <br>巧克宁<br>晓飞",
                category: 2,
              },
              {
                name: "CCP 中国共产党 Uncensored",
                des:
                  "订阅人数 : <br>4<br>重点账号 : <br>William Clinton<br>Zhang Mary",
                category: 2,
              },
              {
                name: "车裂习近平",
                des:
                  "群成员数 : <br>1293<br>重点账号 : <br>小乐 马<br>piao laoshi",
                category: 5,
              },
              {
                name: "🅷🆂君（全tg最大重口群群主本体@Guawang",
                category: 6,
              },
              {
                name: "六纪元三退服务中心",
                des:
                  "群成员数 : <br>1061<br>重点账号 : <br>FBI【共狗殺手】@opop1298<br>叶公子PrinceYe@PrinceYe",
                category: 4,
              },
              {
                name: "一贷一赂",
                category: 6,
              },
              {
                name: "习近平",
                des:
                  "群成员数 : <br>2651<br>重点成员 : <br>一贷一赂 @dingcengsheji<br>霞光@guangxia",
                category: 3,
              },
              {
                name: "维尼国通讯社",
                des:
                  "订阅人数 : <br>945<br>重点账号 : <br>先生（明德） 德<br>モグモグ",
                category: 1,
              },
              {
                name: "「VOP」維尼之聲 - Voice of Pooh",
                des:
                  "订阅人数 : <br>21430<br>重点账号 : <br>Alex Tai<br>中大入境處",
                category: 0,
              },
              {
                name: "Winnie the pooh和它的粉丝们",
                des:
                  "群成员数 : <br>30<br>重点账号 : <br>习近平@wswindows7<br>Lin Jace@Lin_Jace",
                category: 5,
              },
            ],
            links: [
              {
                source: "望野 Visionary",
                target: "習近平和牠的姘頭們",
              },
              {
                source: "燧人氏@askedif",
                target: "習近平和牠的姘頭們",
              },
              {
                source: "習近平和牠的姘頭們",
                target: "中共政治局主持习近平",
              },
              {
                source: "中共政治局主持习近平",
                target: "Vegeta@Lone857857",
              },
              {
                source: "中共政治局主持习近平",
                target: "习近平@wswindows7",
              },
              {
                source: "习近平@wswindows7",
                target: "庆丰末年那些事儿",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "#ccc",
                  },
                },
              },
              {
                source: "Vegeta@Lone857857",
                target: "法外之地",
              },
              {
                source: "庆丰末年那些事儿",
                target: "法外之地",
              },
              {
                source: "庆丰末年那些事儿",
                target: "萌豚中央通讯社（Mengtun News）",
              },
              {
                source: "庆丰末年那些事儿",
                target: "长安街日报",
              },
              {
                source: "庆丰末年那些事儿",
                target: "辱包群",
              },
              {
                source: "法外之地",
                target: "Panzer faust @SiegeofPython",
              },
              {
                source: "法外之地",
                target: "FBI【共狗殺手】@opop1298",
              },
              {
                source: "长安街日报",
                target: "CCP病毒 武汉疫情交流群",
              },
              {
                source: "辱包群",
                target: "习主席治国理念学习讨论小组",
              },
              {
                source: "辱包群",
                target: "郭 大神@xidabi",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "red",
                  },
                },
              },
              {
                source: "Panzer faust @SiegeofPython",
                target: "习主席治国理念学习讨论小组",
              },
              {
                source: "习主席治国理念学习讨论小组",
                target: "郭 大神@xidabi",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "red",
                  },
                },
              },
              {
                source: "习主席治国理念学习讨论小组",
                target: "一贷一赂",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "red",
                  },
                },
              },
              {
                source: "习主席治国理念学习讨论小组",
                target: "习近平",
              },
              {
                source: "FBI【共狗殺手】@opop1298",
                target: "Iee ann @wangchao123234",
              },
              {
                source: "FBI【共狗殺手】@opop1298",
                target: "乳透社",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "#ccc",
                  },
                },
              },
              {
                source: "乳透社",
                target: "噫~这世界",
              },
              {
                source: "乳透社",
                target: "CCP 中国共产党 Uncensored",
              },
              {
                source: "乳透社",
                target: "🅷🆂君（全tg最大重口群群主本体@Guawang",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "#ccc",
                  },
                },
              },
              {
                source: "乳透社",
                target: "维尼国通讯社",
              },
              {
                source: "乳透社",
                target: "六纪元三退服务中心",
              },
              {
                source: "CCP 中国共产党 Uncensored",
                target: "车裂习近平",
              },
              {
                source: "🅷🆂君（全tg最大重口群群主本体@Guawang",
                target: "六纪元三退服务中心",
              },
              {
                source: "🅷🆂君（全tg最大重口群群主本体@Guawang",
                target: "维尼国通讯社",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "#ccc",
                  },
                },
              },
              {
                source: "六纪元三退服务中心",
                target: "习近平",
              },
              {
                source: "六纪元三退服务中心",
                target: "一贷一赂",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "red",
                  },
                },
              },
              {
                source: "维尼国通讯社",
                target: "习近平",
              },
              {
                source: "习近平",
                target: "Winnie the pooh和它的粉丝们",
              },
              {
                source: "一贷一赂",
                target: "习近平",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "red",
                  },
                },
              },
              {
                source: "法外之地",
                target: "「VOP」維尼之聲 - Voice of Pooh",
              },
              {
                source: "FBI【共狗殺手】@opop1298",
                target: "「VOP」維尼之聲 - Voice of Pooh",
                lineStyle: {
                  normal: {
                    type: "dotted",
                    color: "#ccc",
                  },
                },
              },
              {
                source: "乳透社",
                target: "「VOP」維尼之聲 - Voice of Pooh",
              },
              {
                source: "习近平",
                target: "「VOP」維尼之聲 - Voice of Pooh",
              },
            ],
            categories,
          },
        ],
        animationEasingUpdate: "quinticInOut", // 数据更新动画的缓动效果。[ default: cubicOut ]    "quinticInOut"
        animationDurationUpdate: 100, // 数据更新动画的时长。[ default: 300 ]
      };
      chart.setOption(option);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
@import url("./policyAnalyze2.less");
</style>
