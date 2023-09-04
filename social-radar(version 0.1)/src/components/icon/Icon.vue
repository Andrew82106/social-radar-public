 <template>
  <div>
    <div class="icon_top"></div>
    <div class="icon_right" @click="iconClick"></div>
    <div class="icon_bottom"></div>
    <div class="icon_left"></div>
  </div>
</template>
<script>
export default {
  name: "Icon",
  methods: {
    iconClick() {
      this.$emit("icon-click");
    },
  },
};
</script>
<style lang="less">
.icon_top {
  width: 12px;
  height: 12px;
  position: absolute;
  left: 0;
  top: 0;
  border-top: 2px solid #63bbf1;
  border-left: 2px solid #63bbf1;
}
.icon_right {
  width: 12px;
  height: 12px;
  position: absolute;
  right: 0;
  top: 0;
  border-top: 2px solid #63bbf1;
  border-right: 2px solid #63bbf1;
}
.icon_bottom {
  width: 12px;
  height: 12px;
  position: absolute;
  right: 0;
  bottom: 0;
  border-bottom: 2px solid #63bbf1;
  border-right: 2px solid #63bbf1;
}
.icon_left {
  width: 12px;
  height: 12px;
  position: absolute;
  left: 0;
  bottom: 0;
  border-bottom: 2px solid #63bbf1;
  border-left: 2px solid #63bbf1;
}
</style>