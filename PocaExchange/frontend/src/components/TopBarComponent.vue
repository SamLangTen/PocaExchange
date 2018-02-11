<template>
  <el-header>
    <el-row>
      <el-col :md="12" :sm="9" :xs="6"><h1><span class="el-icon-message"/>Pocae</h1></el-col>    
      <el-col :offset="3" :md="9" :sm="12" :xs="15">
        <el-button type="primary">Login</el-button> 
        <el-dropdown>
          <el-button type="primary">
            Postcard<i class="el-icon-arrow-down el-icon--right"></i>
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>Bottles</el-dropdown-item>
            <el-dropdown-item>Request</el-dropdown-item>
            <el-dropdown-item>Response</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-button type="primary">Help</el-button>
      </el-col> 
    </el-row>
  </el-header>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({});
</script>
<style>
.el-row > .el-col > h1 {
  color: #ffffff;
  margin-top: 15px;
  margin-bottom: 14px;
}
.el-row > .el-col > button {
  margin-top: 10px;
  margin-bottom: 10px;
}
.el-row > .el-col > .el-dropdown {
  margin-top: 10px;
  margin-bottom: 10px;
}
.el-row {
  height: inherit;
}
.el-header {
  width: 100%;
  padding: 0px;
  margin: 0px;
  background-color: #409eff;
}
@media (min-width: 1000px ){
  .el-header > .el-row {
    width: 50%;
    margin: auto;
  }
}
@media (max-width: 1500px ) {
  .el-header > .el-row {
    width: 90%;
    margin: auto;
  }
}
</style>
