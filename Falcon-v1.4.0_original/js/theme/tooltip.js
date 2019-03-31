'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Tootltip [bootstrap 4]
-----------------------------------------------*/
utils.$document.ready(() => {
  // https://getbootstrap.com/docs/4.0/components/tooltips/#example-enable-tooltips-everywhere
  $('[data-toggle="tooltip"]').tooltip({ container: '.content' });
  $('[data-toggle="popover"]').popover({ container: '.content' });
});
