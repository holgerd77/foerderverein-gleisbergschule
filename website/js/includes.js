(function () {
  var page = location.pathname.split('/').pop() || 'index.html';

  function includeHTML(id, file) {
    fetch(file)
      .then(function (res) { return res.text(); })
      .then(function (html) {
        var el = document.getElementById(id);
        if (!el) return;
        el.innerHTML = html;
        el.querySelectorAll('a[href="' + page + '"]').forEach(function (a) {
          a.classList.add('active');
        });
      });
  }

  includeHTML('site-header', 'header.html');
  includeHTML('site-footer', 'footer.html');
})();
