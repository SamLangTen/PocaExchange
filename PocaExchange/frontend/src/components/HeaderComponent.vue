<template>
  <div class="headerWrapper">
    <el-row>
      <el-col :span="12"><h1>Pocae</h1></el-col>
      <el-col :span="9">
        <el-menu mode="horizontal">
          <el-menu-item index="1">Login</el-menu-item>
          <el-submenu index="2">
            <template slot="title">Postcard</template>
            <el-menu-item index="2-1">Bottle</el-menu-item>
            <el-menu-item index="2-2">Request</el-menu-item>
            <el-menu-item index="2-3">Response</el-menu-item>
          </el-submenu>
          <el-menu-item index="3">Help</el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  
})
</script>
<style>
  .headerWrapper{
    border-bottom: solid 1px #e6e6e6;
  }
  .el-menu--horizontal{
    border-bottom: 0px;
  }
</style>
