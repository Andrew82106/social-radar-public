<template>
  <div class="PoliticsInfo">
    <Head :title="title"></Head>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <!-- 时间选择器 -->
        <div class="selectTime">
          <span
            v-show="timeSum > 0 && timeSum < 60"
            style="
              color: rgba(255, 255, 255, 0.68);
              display: inline-block;
              margin-right: 10px;
            "
            >({{ timeSum }}s)</span
          >
          <el-date-picker
            v-model="timevalue"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            @change="getDateValue()"
          ></el-date-picker>
          <button
            @click="stopTimer"
            style="background: transparent; color: #fff; border: 1px solid #fff"
          >
            stop
          </button>
          <img
            src="../../assets/img/tianjia.png"
            alt
            style="margin-left: 10px"
            @click="goAdd"
          />
        </div>

        <div class="container">
          <div class="pageView common">
            <icon></icon>
            <a
              href="http://172.29.1.3:8091"
              style="color: white; font-weight: 500"
              >数据总量</a
            >
            <div class="view_box">
              <p style="margin-bottom: 1.25rem; font-weight: 500">
                总量：
                <span>{{ visitCount.data.totalRows }}</span>
              </p>
              <ul class="viewCount">
                <li
                  class="everyView"
                  v-for="(item, index) in locationVist"
                  :key="index"
                >
                  <span>{{ item.source }}</span>
                  <span>：</span>
                  <span>{{ item.total }}</span>
                </li>
              </ul>
              <ul class="language">
                <li v-for="(item, index) in lanVisit" :key="index">
                  <span>{{ item.source }}</span>
                  <span>:</span>
                  <span>{{ item.total }}</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="mapChina common">
            <icon></icon>
            <div id="myChartMap" class="mapStyle"></div>
            <ul class="eventBox">
              <li
                class="events_introduced"
                v-for="(item, index) in infoArr"
                :key="index"
                @click="goDetail(item)"
              >
                <div class="events_introduced_box">
                  <div class="danger_leave">
                    <div>
                      <img
                        src="../../assets/img/danger1.png"
                        alt
                        v-if="item.grade == 1"
                      />
                      <img
                        src="../../assets/img/danger2.png"
                        alt
                        v-if="item.grade == 2"
                      />
                      <img
                        src="../../assets/img/danger3.png"
                        alt
                        v-if="item.grade == 3"
                      />
                      <img
                        src="../../assets/img/danger4.png"
                        alt
                        v-if="item.grade == 4"
                      />
                      <img
                        src="../../assets/img/danger5.png"
                        alt
                        v-if="item.grade == 5"
                      />
                      <p v-if="item.grade == 1" style="color: #741b33">一级</p>
                      <p v-if="item.grade == 2" style="color: #773f3b">二级</p>
                      <p v-if="item.grade == 3" style="color: #7b8744">三级</p>
                      <p v-if="item.grade == 4" style="color: #b7f2f9">四级</p>
                      <p v-if="item.grade == 5" style="color: #e6ccff">五级</p>
                    </div>
                  </div>
                  <div class="event_desc_box">
                    <div class="event_desc">
                      <div class="event_desc_top">
                        <p class="event_title">{{ item.title }}</p>
                        <div class="event_time_add">
                          <div class="event_time" v-if="item.type == 1">
                            <img
                              src="../../assets/img/shijian.png"
                              alt
                              class="timeIcon icon"
                            />
                            <span>{{ item.createTime }}</span>
                          </div>
                          <div class="event_address" v-if="item.type == 1">
                            <img
                              src="../../assets/img/weizhi.png"
                              alt
                              class="addressIcon icon"
                            />
                            <span>{{ item.address }}</span>
                          </div>
                          <div class="event_effect">
                            <p style="margin-right: 0.25rem">影响力指标</p>
                            <div class="effect_con">
                              <div
                                class="effect_proportion"
                                :style="'width:' + item.impactIndicators + '%'"
                              ></div>
                            </div>
                            <p>{{ item.impactIndicators }}%</p>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="events_content" v-if="item.type == 1">
                      {{ item.synopsis }}
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          <div class="pageRight">
            <div class="common warning">
              <icon></icon>
              <p class="title">事件预警</p>

              <swiper
                :options="swiperOption"
                ref="mySwiper"
                v-if="warningList.length != 0"
                class="swiper"
              >
                <swiper-slide
                  v-for="(item, index) in this.warningList"
                  :key="index"
                  class="swiper-slide"
                >
                  <li @click="goEventDetail(item.id, index)">
                    <img src="../../assets/img/yujing.png" alt />
                    <p>{{ item.title }}</p>
                  </li>
                </swiper-slide>
              </swiper>
            </div>

            <div class="common topic">
              <icon></icon>
              <p class="title">话题分布</p>
              <div class="select_local">
                <el-select v-model="value" placeholder="请选择">
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.label"
                  ></el-option>
                </el-select>
              </div>
              <div id="myChartZhu"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "../../../static/js/chinamap/china.js";
import "swiper/dist/css/swiper.css";
import Head from "../../components/Head/Head.vue";
import Icon from "../../components/Icon/Icon.vue";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import visitCount from "../../untils/visitCount.js"; //访问量数据
import warning from "../../untils/warning.js"; //事件预警数据
import topic from "../../untils/topic.js"; //话题分布数据
import newsetDate from "../../untils/newsetDate.js"; //地图数据和列表页数据合计
import "../../../node_modules/echarts/map/js/world.js";

var vm;
var timer;
var timersum;
export default {
  name: "PoliticsInfo",
  components: {
    Head,
    Icon,
    swiper,
    swiperSlide,
  },
  created() {
    // 访问量数据处理
    let visitCount = this.visitCount.data.resultList;
    for (var i = 0; i < visitCount.length; i++) {
      if (visitCount[i].type == 1) {
        this.locationVist.push(visitCount[i]);
      } else if (visitCount[i].type == 2) {
        this.lanVisit.push(visitCount[i]);
      }
    }

    //时间预警数据
    this.warningList = warning.data.resultList;
    //话题分布数据处理
    let topicMes = topic.data.resultList;
    for (let i = 0; i < topicMes.length; i++) {
      let obj = {
        value: topicMes[i].id,
        label: topicMes[i].source,
      };
      this.options.push(obj);
      this.topicList.push(topicMes[i]);
    }
    //设置多选框默认数据
    this.value = this.options[0].label;
    this.getZheDate();
    this.dataBox = newsetDate.data.resultList;
    this.dataBox.sort((a, b) => b.impactIndicators - a.impactIndicators);
    console.log(this.dataBox);
  },
  data() {
    return {
      title: "网络危安信息管控与决策支持系统", //页面标题
      timeSum: 60, //倒计时
      // timevalue: [
      //   "Wed Jul 31 2019 00:00:00 GMT+0800",
      //   "Wed Jul 31 2019 00:00:00 GMT+0800"
      // ], //时间段选择
      timevalue: ["2019-06-13", "2020-01-13"], //时间段选择
      warningList: [],

      options: [],
      value: "",
      valueId: "",
      // 预警轮播配置
      swiperOption: {
        slidesPerView: 5,
        centeredSlides: true,
        watchSlidesProgress: true,
        // slidesOffsetBefore: 5,
        autoplay: {
          delay: 200000, //1.5秒切换一次
          disableOnInteraction: false,
        },

        freeMode: true,
        loop: true,
        direction: "vertical",
        autoplayDisableOnInteraction: false,
        observer: true, //修改swiper自己或子元素时，自动初始化swiper
        observeParents: true, //修改swiper的父元素时，自动初始化swiper
      },
      // 访问量数据
      visitCount: visitCount,
      locationVist: [],
      lanVisit: [],
      topicList: [],
      // 柱状图数据
      xData: [],
      yData: [],
      option: {},
      // 地图数据与列表页数据合集
      mapDate: [], // 地图数 据
      infoArr: [], //当前时间段内发生的事件
      dataBox: [],
      myChartMap: "",
      mapoption: [],
    };
  },

  mounted() {
    this.upMapDate();
    let _this = this;
    timer = setInterval(() => {
      _this.timevalue[0] = new Date(
        new Date(_this.timevalue[0]).getTime() - 24 * 60 * 60 * 1000
      );
      _this.timevalue[1] = new Date(
        new Date(_this.timevalue[1]).getTime() - 24 * 60 * 60 * 1000
      );
      _this.timevalue = [_this.timevalue[0], _this.timevalue[1]];
      _this.upMapDate();
      if (new Date(_this.timevalue[0]).getTime() <= 1563580800000) {
        clearInterval(timer);
      }
    }, 200000);
    console.log(new Date("2019-07-20").getTime());

    this.getzhu();
  },
  destroyed() {
    clearInterval(timer);
    clearInterval(timersum);
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.swiper;
    },
  },
  watch: {
    value(newValue, oldValue) {
      if (newValue != oldValue) {
        this.getZheDate();
        this.getzhu();
      }
    },
    timeSum(newValue, oldValue) {
      if (newValue <= 0) {
        let _this = this;
        clearInterval(timersum);
        this.timeSum = 60;
        if (new Date(_this.timevalue[0]).getTime() <= 1563580800000) {
        } else {
          timer = setInterval(() => {
            _this.timevalue[0] = new Date(
              new Date(_this.timevalue[0]).getTime() - 24 * 60 * 60 * 1000
            );
            _this.timevalue[1] = new Date(
              new Date(_this.timevalue[1]).getTime() - 24 * 60 * 60 * 1000
            );
            _this.upMapDate();
            _this.timevalue = [_this.timevalue[0], _this.timevalue[1]];
            if (new Date(_this.timevalue[0]).getTime() <= 1563580800000) {
              clearInterval(timer);
            }
          }, 2000);
        }
      }
    },
  },
  methods: {
    stopTimer() {
      clearInterval(timer);
      clearInterval(timersum);
      this.timeSum = 60;
    },
    //更新列表和地图上的数据
    upMapDate() {
      // 重置数据
      this.infoArr = [];
      this.mapDate = [];
      this.mapoption = [];

      this.getAllData(); //获取数据
      this.drowlineMap(); //中国地图
    },

    // 处理列表页和地图的数据
    getAllData() {
      // 处理列表页数据
      // 先获取在当前时间内的数据
      // 获得开始和结束的时间（不带时分秒）
      let current_start = this.getStartTime(
        new Date(this.timevalue[0]).getTime()
      );
      let current_end = this.getStartTime(
        new Date(this.timevalue[1]).getTime()
      );
      // console.log(this.timevalue[0], this.timevalue[1]);
      // 获得开始和结束的时间戳（不带时分秒）
      let current_start_tamp = new Date(current_start).getTime();
      let current_end_tamp = new Date(current_end).getTime();
      for (let i = 0; i < this.dataBox.length; i++) {
        let everyTamp = new Date(
          this.dataBox[i].createTime.split(" ")[0]
        ).getTime();
        if (everyTamp >= current_start_tamp && everyTamp <= current_end_tamp) {
          this.infoArr.push(this.dataBox[i]);
        }
      }
      for (let j = 0; j < this.infoArr.length; j++) {
        var obj = { name: "", value: [] };
        this.mapDate.push(obj);
        this.mapDate[j].name = this.infoArr[j].title;
        this.mapDate[j].value.push(this.infoArr[j].longitude);
        this.mapDate[j].value.push(this.infoArr[j].latitude);
        console.log(this.infoArr[j].number);
        if (this.infoArr[j].number > 100 && this.infoArr[j].number < 1000) {
          this.mapDate[j].value.push(this.infoArr[j].number / 10);
        } else if (
          this.infoArr[j].number >= 1000 &&
          this.infoArr[j].number < 10000
        ) {
          this.mapDate[j].value.push(this.infoArr[j].number / 100);
        } else if (
          this.infoArr[j].number >= 10000 &&
          this.infoArr[j].number < 100000
        ) {
          this.mapDate[j].value.push(this.infoArr[j].number / 1000);
        } else if (this.infoArr[j].number >= 100000) {
          this.mapDate[j].value.push(this.infoArr[j].number / 10000);
        } else {
          this.mapDate[j].value.push(this.infoArr[j].number);
        }
        this.mapDate[j].value.push(this.infoArr[j].number);
      }
    },
    // 去涉政信息详情页或群体事件详情页
    goDetail(item) {
      if (item.type == 2) {
        this.$router.push({
          path: "/policyanalyze",
          query: {
            item: JSON.stringify(item),
          },
        });
      } else if (item.type == 1) {
        this.$router.push({
          path: "/group",
          query: {
            item: JSON.stringify(item),
          },
        });
      } else if (item.type == 3) {
        this.$router.push({
          path: "/policyanalyze2",
          query: {
            item: JSON.stringify(item),
          },
        });
      }
    },
    // 将new Date 的时间格式转换成1-1-1的时间格式
    getStartTime(time) {
      let date = new Date(time);
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var day = date.getDate();
      if (month < 10) {
        month = "0" + month;
      }
      if (day < 10) {
        day = "0" + day;
      }
      let timeDetail = year + "-" + month + "-" + day;
      return timeDetail;
    },
    getDateValue() {
      clearInterval(timersum);
      clearInterval(timer);
      timersum = setInterval(() => {
        this.timeSum--;
      }, 1000);
      this.upMapDate();
    },
    // 实例化中国地图

    drowlineMap() {
      // 基于准备好的dom，初始化echarts实例
      this.myChartMap = this.$echarts.init(
        document.getElementById("myChartMap")
      );
      function randomData() {
        return Math.round(Math.random() * 2500);
      }
      // 指定图表的配置项和数据
      this.mapoption = {
        backgroundColor: "rgba(9,39,93,0.26)",
        geo: {
          name: "中国",
          type: "map",
          map: "world",
          roam: true, //开启鼠标缩放和平移漫游。
          zoom: 5, //缩放比例，
          center: [114.2, 22.3],
          label: {
            //图中文本的样式
            normal: {
              show: false, //地图上的文本标签不显示
            },
            emphasis: {
              show: false,
            },
          },
          emphasis: {
            label: {
              show: false,
            },
          },

          itemStyle: {
            borderColor: "#10A5EE", //边界线颜色
            borderWidth: 2,
            shadowOffsetY: 0,
            shadowOffsetX: 0,
            shadowColor: "red",
            areaColor: "rgba(9,39,93,0.26)", //区域颜色
            emphasis: {
              // 高亮状态下的样式
              areaColor: "rgba(9,39,93,0.26)",
            },
          },
        },
        series: [
          {
            type: "scatter", // series图表类型
            coordinateSystem: "geo", // series坐标系类型

            itemStyle: {
              normal: {
                color: "#C9852F",
                shadowBlur: 10,
                shadowColor: "#333",
              },
            },
            data: this.mapDate,
            symbolSize: function (val) {
              return val[2] / 5;
            },
            label: {
              normal: {
                //隐藏延时
                hideDelay: 100,
                //背景颜色
                backgroundColor: "rgba(68,77,85,0.8)",
                //边框圆角
                borderRadius: 8,
                //内边距
                padding: [10, 10],
                //鼠标是否可以进入提示框
                color: "#fff",
                formatter: function (params) {
                  return (
                    params.data.name + "\n" + "人数 : " + params.data.value[3]
                  );
                },
                position: "right",
                show: false,
              },
              emphasis: {
                show: true,
              },
            },
          },
        ],
      };
      this.myChartMap.clear();
      this.myChartMap.setOption(this.mapoption);
    },

    // 实例化柱状图
    getzhu() {
      this.myChart = this.$echarts.init(document.getElementById("myChartZhu"));
      var dataAxis = this.xData;
      var data = this.yData;
      var yMax = 500;
      var dataShadow = [];

      for (var i = 0; i < data.length; i++) {
        dataShadow.push(yMax);
      }

      this.option = {
        tooltip: {
          show: true,
        },
        xAxis: {
          data: dataAxis,
          axisLabel: {
            textStyle: {
              color: "#fff",
            },
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            show: false,
          },
          z: 10,
        },
        yAxis: {
          min: 0,
          max: 900,
          interval: 100,
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed",
            },
          },
          grid: {
            left: 35,
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: "#fff",
              type: "solid",
            },
          },
          axisTick: {
            show: false,
          },
          axisLabel: {
            textStyle: {
              color: "#999",
            },
          },
        },
        dataZoom: [
          {
            type: "inside",
          },
        ],
        series: [
          {
            // For shadow
            type: "bar",
            itemStyle: {
              color: "rgba(0,0,0,0.05)",
            },
            barGap: "-100%",
            barCategoryGap: "40%",
            data: dataShadow,
            animation: false,
          },
          {
            type: "bar",
            itemStyle: {
              color: " #827EE4",
            },
            emphasis: {
              itemStyle: {
                color: this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "#2378f7" },
                  { offset: 0.7, color: "#2378f7" },
                  { offset: 1, color: "#83bff6" },
                ]),
              },
            },
            data: data,
          },
        ],
      };
      this.myChart.clear();
      this.myChart.setOption(this.option);

      // Enable data zoom when user click bar.
      var zoomSize = 6;
    },
    // 柱状图数据处理
    getZheDate() {
      // 柱状图数据设置
      let zheData = [];
      // 重置数据横轴和纵轴数据
      this.xData = [];
      this.yData = [];
      for (let i = 0; i < this.topicList.length; i++) {
        if (this.topicList[i].source == this.value) {
          zheData = this.topicList[i].topictList;
        }
      }
      for (let i = 0; i < zheData.length; i++) {
        // 设置折线图默认横轴数据
        this.xData.push(zheData[i].topict);
        // 设置折线图默认纵轴数据
        this.yData.push(zheData[i].total);
      }
    },
    // 去添加页面
    goAdd() {
      this.$router.push("/addmes");
    },
    goEventDetail(e, y) {
      console.log(55555555555);
      console.log(e, y);
      for (let i = 0; i < this.dataBox.length; i++) {
        if (e == this.dataBox[i].id) {
          if (this.dataBox[i].type == 1) {
            this.$router.push({
              path: "/group",
              query: {
                item: JSON.stringify(this.dataBox[i]),
              },
            });
          } else {
            this.$router.push({
              path: "/policyanalyze",
              query: {
                item: JSON.stringify(this.dataBox[i]),
              },
            });
          }
        }
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
@import url("./PoliticsInfo.less");
/deep/ .el-input {
  input {
    background: transparent;
    border: 1px solid #fff;
    color: #fff;
    padding-left: 0.625rem !important;
    padding: 0;
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
/deep/ .el-date-editor .el-range__icon {
  font-size: 1.125rem !important;
}
</style>
