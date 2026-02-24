(function () {
  var scriptSrc = document.currentScript.getAttribute('src');
  var base = scriptSrc.replace(/js\/includes[^/]*\.js$/, '');
  var page = location.pathname.split('/').pop() || 'index.html';

  function includeHTML(id, file) {
    fetch(base + file)
      .then(function (res) { return res.text(); })
      .then(function (html) {
        var el = document.getElementById(id);
        if (!el) return;
        el.innerHTML = html;
        if (base) {
          el.querySelectorAll('[href],[src]').forEach(function (node) {
            ['href', 'src'].forEach(function (attr) {
              var val = node.getAttribute(attr);
              if (val && !val.startsWith('http') && !val.startsWith('/') &&
                  !val.startsWith('#') && !val.startsWith('mailto:')) {
                node.setAttribute(attr, base + val);
              }
            });
          });
        }
        el.querySelectorAll('a').forEach(function (a) {
          if (a.getAttribute('href').endsWith(page)) {
            a.classList.add('active');
          }
        });
      });
  }

  includeHTML('site-header', 'header.html');
  includeHTML('site-footer', 'footer.html');
})();
