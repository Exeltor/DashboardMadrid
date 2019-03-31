'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Owl Carousel
-----------------------------------------------*/
const $carousel = $('.owl-carousel');
utils.$document.ready(() => {
  if ($carousel.length) {
    const Selector = {
      ALL_TIMELINE: '*[data-zanim-timeline]',
      ACTIVE_ITEM: '.owl-item.active',
    };
    const owlZanim = {
      zanimTimeline($el) {
        return $el.find(Selector.ALL_TIMELINE);
      },
      play($el) {
        if (this.zanimTimeline($el).length === 0) return;
        $el.find(`${Selector.ACTIVE_ITEM} > ${Selector.ALL_TIMELINE}`).zanimation((animation) => {
          animation.play();
        });
      },
      kill($el) {
        if (this.zanimTimeline($el).length === 0) return;
        this.zanimTimeline($el).zanimation((animation) => {
          animation.kill();
        });
      },
    };

    $carousel.each((index, value) => {
      const $this = $(value);
      const options = $this.data('options') || {};
      utils.isRTL() && (options.rtl = true);

      options.navText || (options.navText = ['<span class="fas fa-angle-left"></span>', '<span class="fas fa-angle-right"></span>']);
      options.touchDrag = true;

      $this.owlCarousel($.extend(options || {}, {
        onInitialized(event) {
          owlZanim.play($(event.target));
        },
        onTranslate(event) {
          owlZanim.kill($(event.target));
        },
        onTranslated(event) {
          owlZanim.play($(event.target));
        },
      }));
    });
  }
});
