'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Countdown
-----------------------------------------------*/
utils.$document.ready(() => {
  const $dataCountdowns = $('[data-countdown]');
  const DATA_KEY = {
    FALLBACK: 'countdown-fallback',
    COUNTDOWN: 'countdown',
  };

  if ($dataCountdowns.length) {
    $dataCountdowns.each((index, value) => {
      const $dateCountdown = $(value);
      const date = $dateCountdown.data(DATA_KEY.COUNTDOWN);
      let fallback;

      if (typeof $dateCountdown.data(DATA_KEY.FALLBACK) !== typeof undefined) {
        fallback = $dateCountdown.data(DATA_KEY.FALLBACK);
      }

      $dateCountdown.countdown(date, (event) => {
        if (event.elapsed) {
          $dateCountdown.text(fallback);
        } else {
          $dateCountdown.text(event.strftime('%D days %H:%M:%S'));
        }
      });
    });
  }
});
