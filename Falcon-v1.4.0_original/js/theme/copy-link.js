'use strict';

import utils from './Utils';
/*-----------------------------------------------
|   Copy link
-----------------------------------------------*/
utils.$document.ready(() => {
  $('#copyLinkModal').on('shown.bs.modal', () => {
    $(".invitation-link").focus().select();
  });
});
