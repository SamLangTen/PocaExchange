<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1">Login</el-menu-item>
    <el-menu-item index="2">Exchange</el-menu-item>
    <el-menu-item index="3">Drifting Bottle</el-menu-item>
    </el-menu>
  </div>
</template>
