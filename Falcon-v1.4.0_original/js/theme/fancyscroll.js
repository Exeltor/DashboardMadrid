'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   On page scroll for #id targets
-----------------------------------------------*/
utils.$document.ready(($) => {
  $('a[data-fancyscroll]').click(function scrollTo(e) {
    // const $this = $(e.currentTarget);
    const $this = $(this);
    if (utils.location.pathname === $this[0].pathname && 
utils.location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && 
utils.location.hostname === this.hostname) {
    e.preventDefault();  
    let target = $(this.hash);
      target = target.length ? target : $(`[name=${this.hash.slice(1)}]`);
      if (target.length) {
        $('html,body').animate({
          scrollTop: (target.offset().top - ($this.data('offset') || 0)),
        }, 400, 'swing', () => {
          const hash = $this.attr('href');
          window.history.pushState ?
            window.history.pushState(null, null, hash) : window.location.hash = hash;
        });
        return false;
      }
    }
    return true;
  });

  let { hash } = window.location;

  if(hash && document.getElementById(hash.slice(1))){
    let $this = $(hash);
    $('html,body').animate({
      scrollTop: $this.offset().top - $(`a[href='${hash}']`).data('offset'),
    }, 400, 'swing', () => {
      window.history.pushState ?
        window.history.pushState(null, null, hash) : window.location.hash = hash;
    });
  }
});







