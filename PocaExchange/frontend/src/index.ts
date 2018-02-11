import Vue from "vue";
import HelloComponent from "./components/Hello.vue";
import TopBarComponent from "./components/TopBarComponent.vue";
import ElementUI from 'element-ui';
import "element-ui/lib/theme-chalk/index.css";

Vue.use(ElementUI);

let v = new Vue({
    el: "#app",
    template: `
    <el-container>
        <el-header><TopBarComponent/></el-header>
        <el-main>Main</el-main>
    </el-container>
    `,
    components: {
        TopBarComponent
    }
});