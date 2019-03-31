'use strict';

import utils from './Utils';
/*-----------------------------------------------
|   Count Up
-----------------------------------------------*/
utils.$document.ready(() => {
  const $counters = $('[data-countup]');
  if ($counters.length) {
    $counters.each((index, value) => {
      const $counter = $(value);
      const counter = $counter.data('countup');
      const toAlphanumeric = (num) => {
        let number = num;
        const abbreviations = {
          k: 1000,
          m: 1000000,
          b: 1000000000,
          t: 1000000000000,
        };
        if (num < abbreviations.m) {
          number = `${(num / abbreviations.k).toFixed(2)}k`;
        } else if (num < abbreviations.b) {
          number = `${(num / abbreviations.m).toFixed(2)}m`;
        } else if (num < abbreviations.t) {
          number = `${(num / abbreviations.b).toFixed(2)}b`;
        } else {
          number = `${(num / abbreviations.t).toFixed(2)}t`;
        }
        return number;
      };
      const toComma = num => num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      const toSpace = num => num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
      let playCountUpTriggered = false;
      const countUP = () => {
        if (utils.isScrolledIntoView(value) && !playCountUpTriggered) {
          if (!playCountUpTriggered) {
            $({ countNum: 0 }).animate(
              { countNum: counter.count },
              {
                duration: counter.duration || 1000,
                easing: 'linear',
                step() {
                  $counter.text((counter.prefix ? counter.prefix : '') + Math.floor(this.countNum));
                },
                complete() {
                  switch (counter.format) {
                    case 'comma':
                      $counter.text((counter.prefix ? counter.prefix : '') + toComma(this.countNum));
                      break;
                    case 'space':
                      $counter.text((counter.prefix ? counter.prefix : '') + toSpace(this.countNum));
                      break;
                    case 'alphanumeric':
                      $counter.text((counter.prefix ? counter.prefix : '') + toAlphanumeric(this.countNum));
                      break;
                    default:
                      $counter.text((counter.prefix ? counter.prefix : '') + this.countNum);
                  }
                },
              },
            );
            playCountUpTriggered = true;
          }
        }
        return playCountUpTriggered;
      };
      countUP();
      utils.$window.scroll(() => {
        countUP();
      });
    });
  }
});
