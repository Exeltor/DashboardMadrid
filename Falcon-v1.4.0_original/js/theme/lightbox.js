'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Lightbox
-----------------------------------------------*/
/*
  global lightbox
*/
utils.$document.ready(() => {
  if ($('[data-lightbox]').length) {
    lightbox.option({
      resizeDuration: 400,
      wrapAround: true,
      fadeDuration: 300,
      imageFadeDuration: 300,
    });
  }
});
