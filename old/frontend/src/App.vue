<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style lang="less">
html,
body {
  margin: 0px;
  padding: 0px;
  width: 100%;
  height: 100%;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, SimSun, sans-serif;
  font-size: 14px;
  -webkit-font-smoothing: antialiased;
  background: url("./assets/img/background_img.png") repeat center/100%;
}

#app {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
}
p {
  margin: 0;
  padding: 0;
}
ul {
  margin: 0;
  padding: 0 !important;
}
li {
  list-style: none;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}
input[type="number"] {
  -moz-appearance: textfield;
}
.common {
  position: relative;
  border: 1px solid #20437d;
  text-align: center;
  background:#011A4B;
  box-sizing: border-box;
  -webkit-box-sizing: border-box
}
.title {
  margin-top: 0.9375rem;
  font-size: 1rem;
  margin-bottom:1rem;
}
</style>

