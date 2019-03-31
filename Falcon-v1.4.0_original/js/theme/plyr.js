'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Inline Player [plyr]
-----------------------------------------------*/
/*
  global Plyr
*/
utils.$document.ready(() => {
  const $players = $('.player');
  if ($players.length) {
    $players.each((index, value) => new Plyr($(value), { captions: { active: true } }));
  }
  return false;
});
