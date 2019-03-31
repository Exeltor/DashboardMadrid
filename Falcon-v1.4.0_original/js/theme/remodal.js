'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Remodal [video lightbox]
-----------------------------------------------*/
utils.$document.ready(() => {
  const $videoModals = $('.video-modal');
  if ($videoModals.length) {
    utils.$body.after(`
      <div id='videoModal' class='remodal remodal-video'>
        <button data-remodal-action='close' class='remodal-close'></button>
        <div class='embed-responsive embed-responsive-16by9'>
          <div id='videoModalIframeWrapper'></div>
        </div>
      </div>
    `);
    const $videoModal = $('#videoModal').remodal();
    const $videoModalIframeWrapper = $('#videoModalIframeWrapper');

    $videoModals.each((index, value) => {
      $(value).on('click', (e) => {
        e.preventDefault();

        const $this = $(e.currentTarget);
        const ytId = $this.attr('href').split('/');
        const start = $this.data('start');
        const end = $this.data('end');

        if (ytId[2] === 'www.youtube.com') {
          $videoModalIframeWrapper.html(`<iframe id='videoModalIframe' src='//www.youtube.com/embed/${ytId[3].split('?v=')[1]}?rel=0&amp;autoplay=1&amp;enablejsapi=0&amp;start=${start}&ampend=${end}' allowfullscreen' frameborder='0' class='embed-responsive-item hide'></iframe>`);
        } else if (ytId[2] === 'vimeo.com') {
          $videoModalIframeWrapper.html(`<iframe id='videoModalIframe' src='https://player.vimeo.com/video/${ytId[3]}?autoplay=1&title=0&byline=0&portrait=0 ?autoplay=1&title=0&byline=0&portrait=0 hide'></iframe>`);
        }
        $videoModal.open();
      });
    });

    utils.$document.on('closed', '.remodal', (e) => {
      const $this = $(e.currentTarget);
      if ($this.attr('id') === 'videoModal') {
        $videoModalIframeWrapper.html('');
      }
    });
  }
});
