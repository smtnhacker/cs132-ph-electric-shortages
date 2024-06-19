var links = document.getElementsByTagName("a");

Array.prototype.forEach.call(links, function (elem, index) {
  var elemAttr = elem.getAttribute("href");
  if (elemAttr && elemAttr.includes("#")) {
    elem.addEventListener("click", function (ev) {
      ev.preventDefault();
      document.getElementById(elemAttr.replace(/#/, "")).scrollIntoView({
        behavior: "smooth",
        block: "start",
        inline: "nearest",
      });
    });
  }
});

document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault(); // Prevent default jump to top

    const target = document.getElementById(
      this.getAttribute("href").substring(1)
    );
    const headerHeight = document.querySelector("header").offsetHeight; // Get header height
    const targetTop = target.offsetTop - headerHeight; // Calculate offset for header

    window.scrollTo({
      top: targetTop,
      behavior: "smooth",
    });
  });
});
