let basePath = document.querySelector('.md-logo').href;
let documentPath = document.baseURI.replace(basePath, '');

if (documentPath) {
    document.querySelectorAll('.md-select__link').forEach(function(selector) {
        let url = new URL(selector.href + documentPath, document.baseURI).href;
        fetch(url, {
            method: 'HEAD'
          })
        .then(function(response) {
            if (response.status === 200) {
                selector.href += documentPath;
            }
        });
    });
}