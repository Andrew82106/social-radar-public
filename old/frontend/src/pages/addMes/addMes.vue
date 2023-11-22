<template>
  <div class="PoliticsInfo">
    <Head :title="title"></Head>
    <div class="PoliticsInfoBox">
      <div class="InfoWrap">
        <div class="edit_box common">
          <Icon></Icon>
          <div class="edit">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td valign="top">群体事件标题：</td>
                <td valign="top">
                  <input type="text" placeholder="请输入标题" class="titleInput" />
                </td>
                <td valign="top">
                  <div class="search_input">
                    <input type="text" />
                    <div class="btn">
                      <img src="../../assets/img/juxing1.png" alt />
                      <p class="searchBtn">搜索</p>
                    </div>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">事件介绍：</td>
                <td valign="top" style="height:150px">
                  <textarea name id cols="30" rows="10" placeholder="请输入内容"></textarea>
                </td>
                <td rowspan="4" valign="top">
                  <div class="search_resault"></div>
                </td>
              </tr>
              <tr>
                <td valign="top">群体事件时间：</td>
                <td valign="top" style="height:55px">
                  <el-date-picker v-model="value1" type="date" placeholder="选择日期"></el-date-picker>
                </td>
              </tr>
              <tr>
                <td valign="top">关键词：</td>
                <td valign="top" style="height:80px">
                  <div class="news_div">
                   
                    <el-select v-model="value2" multiple collapse-tags placeholder="请选择">
                      <el-option
                        v-for="item in news_options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                      ></el-option>
                    </el-select>
                  </div>
                </td>
              </tr>
              <tr>
                <td valign="top">标签集：</td>
                <td valign="top" style="height:80px">
                  <div class="lable_box">
                    <ul class="lable">
                      <li>
                        <input type="checkbox" />
                        <label for>群体性事件</label>
                      </li>
                      <li>
                        <input type="checkbox" />
                        <label for>涉政事件</label>
                      </li>
                    </ul>
                  </div>
                </td>
              </tr>
            </table>
          </div>
          <div class="save">
            <div class="saveDiv">
              <img src="../../assets/img/juxing.png" alt />
              <p class="saveBtn">保存</p>
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

var vm;
var timer;
export default {
  name: "AddMes",
  components: {
    Head,
    Icon
  },
  data() {
    return {
      title: "涉政信息分析系统", //页面标题
      value1: "",
      value2: "",
      news_options: [
        {
          value: "选项1",
          label: "机场"
        },
        {
          value: "选项2",
          label: "反修例"
        },
        {
          value: "选项3",
          label: "中环"
        },
        {
          value: "选项4",
          label: "恶法"
        },
        {
          value: "选项5",
          label: "人权"
        },
        {
          value: "选项6",
          label: "集会"
        },
        {
          value: "选项7",
          label: "游行"
        },
        {
          value: "选项8",
          label: "快闪"
        },
        {
          value: "选项9",
          label: "共党"
        },
        {
          value: "选项10",
          label: "示威"
        },
        {
          value: "选项11",
          label: "诉讼"
        },
      ]
    };
  },
  created() {},
  mounted() {},
  destroyed() {},
  methods: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
@import url("./addMes.less");
/deep/ .el-input {
  input {
    background: transparent;
    border: 1px solid #fff;
    color: #fff;
    padding: 0;
    padding-left: 2.625rem;
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
/deep/ .el-date-editor.el-input,
.el-date-editor.el-input__inner {
  width: 100%;
}
/deep/ .el-select {
  width: 100% !important;
}
</style>
