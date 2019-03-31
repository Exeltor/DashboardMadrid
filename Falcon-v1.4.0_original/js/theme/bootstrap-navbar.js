'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Top navigation opacity on scroll
-----------------------------------------------*/
utils.$document.ready(() => {
  const $navbar = $('.navbar-theme');

  if ($navbar.length) {
    const windowHeight = utils.$window.height();
    utils.$window.scroll(() => {
      const scrollTop = utils.$window.scrollTop();
      let alpha = (scrollTop / windowHeight) * 2;

      (alpha >= 1) && (alpha = 1);
      $navbar.css({ 'background-color': `rgba(11, 23, 39, ${alpha})` });
    });

    // Fix navbar background color [after and before expand]
    const classList = $navbar.attr('class').split(' ');
    const breakpoint = classList.filter(c => c.indexOf('navbar-expand-') >= 0)[0].split('navbar-expand-')[1];
    utils.$window.resize(() => {
      if (utils.$window.width() > utils.breakpoints[breakpoint]) {
        return $navbar.removeClass('bg-dark');
      } else if (!$navbar.find('.navbar-toggler').hasClass('collapsed')) {
        return $navbar.addClass('bg-dark');
      }
      return null;
    });

    // Top navigation background toggle on mobile
    $navbar.on('show.bs.collapse hide.bs.collapse', (e) => {
      $(e.currentTarget).toggleClass('bg-dark');
    });
  }
});
