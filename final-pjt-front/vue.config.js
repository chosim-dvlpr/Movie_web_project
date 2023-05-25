const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// module.exports = {
//   // ...
//   configureWebpack: {
//     // ...
//     plugins: [
//       // ...
//       new Dotenv({
//         path: './.env.local',
//         safe: true,
//         systemvars: true,
//         silent: true,
//         defaults: false
//       })
//     ]
//   }
// };
