module.exports = {
    plugins: [
      require('cssnano')(),
      require('postcss-sourcemaps')() // เพิ่มปลั๊กอินเพื่อสร้างแผนที่ CSS
    ]
  };
  