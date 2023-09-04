 <template>
  <div class="head">
    <div class="wrap">
      <div class="head_left" v-if="isshow" @click="goBack">
        <span style="text-align:center;display:inline-block;margin-right:10px;">
          <img src="../../assets/img/left_arrow.png" alt style="width:9px;height:13xp;" />
        </span>
        <span style="color:#ffffff;">{{name}}</span>
      </div>
      <div class="head_title">
        <img src="../../assets/img/left_icon.png" alt />
        <span>{{title}}</span>
        <img src="../../assets/img/right_icon.png" alt class="img_right" />
      </div>
    </div>
  </div>
</template>

<script>
import sa from "../../assets/img/left_icon.png";
export default {
  name: "Head",
  data() {
    return {};
  },
  props: {
    isshow: {
      type: Boolean,
      required: false,
      default: false
    },
    name: {
      type: String,
      required: false,
      default: ""
    },
    title: {
      type: String,
      require: false,
      default: "涉政信息分析系统"
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    }
  }
};
</script>

<style lang="less" scope>
.head {
 
  height: 10%;
  line-height: 90px;
  text-align: center;
  width: 100%;
  color: #26cff3;
  box-sizing: border-box;
  border-bottom: 1px solid rgba(37, 75, 136, 1);
  .wrap {
    width: 96%;
    height: 100%;
    margin: 0 auto;
     position: relative;
     display: flex;
     justify-content: space-around;
    .head_left {
      position: absolute;
      left:0;
 0  
      height: 100%;
    }
    .head_title {
      font-size: 22px;
      display: inline-block;
      display: flex;
     
      align-items: center;
      img {
        width: 155px;
        height: 21px;
      }
      span{
        display: inline-block;
        margin:0 1.25rem;
      }
    }
  }
}
</style>
