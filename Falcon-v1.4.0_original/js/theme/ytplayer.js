'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   YTPlayer
-----------------------------------------------*/
utils.$document.ready(() => {
  const Selector = {
    BG_YOUTUBE: '.bg-youtube',
    BG_HOLDER: '.bg-holder',
  };
  const DATA_KEY = { PROPERTY: 'property' };
  const $youtubeBackground = $(Selector.BG_YOUTUBE);

  if ($youtubeBackground.length) {
    $youtubeBackground.each((index, value) => {
      const $this = $(value);
      console.log($this.data(DATA_KEY.PROPERTY));
      $this.data(DATA_KEY.PROPERTY, $.extend($this.data(DATA_KEY.PROPERTY), {
        showControls: false,
        loop: true,
        autoPlay: true,
        mute: true,
        containment: $this.parent(Selector.BG_HOLDER),
      }));
      $this.YTPlayer();
    });
  }
});
