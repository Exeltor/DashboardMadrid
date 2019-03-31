window.utils.$document.ready(() => {
  const { utils } = window;
  const { $window, breakpoints } = utils;
  let navDropShadowFlag = true;
  const CLASS_NAME = {
    navbarGlassShadow: 'navbar-glass-shadow',
    collapsed: 'collapsed',
  };
  const SELECTOR = {
    navbar: '.navbar:not(.navbar-vertical)',
    navbarVertical: '.navbar-vertical',
    navbarToggler: '.navbar-toggler',
    navbarVerticalCollapse: '#navbarVerticalCollapse',
  };
  const $navbar = $(SELECTOR.navbar);
  const $navbarVerticalCollapse = $(SELECTOR.navbarVerticalCollapse);

  const setDropShadow = ($elem) => {
    if ($elem.scrollTop() > 0 && navDropShadowFlag) {
      $navbar.addClass(CLASS_NAME.navbarGlassShadow);
    } else {
      $navbar.removeClass(CLASS_NAME.navbarGlassShadow);
    }
  };
  let breakPoint;
  const navbarVerticalClass = $(SELECTOR.navbarVertical).attr('class');
  if (navbarVerticalClass) {
    breakPoint = breakpoints[navbarVerticalClass
      .split(' ')
      .filter(cls => cls.indexOf('navbar-expand-') === 0)
      .pop()
      .split('-')
      .pop()];
  }
  $window.on('load scroll', () => setDropShadow($window));
  $navbarVerticalCollapse.on('scroll', () => {
    navDropShadowFlag = true;
    setDropShadow($navbarVerticalCollapse);
  });
  $navbarVerticalCollapse.on('show.bs.collapse', () => {
    if ($window.width() < breakPoint) {
      navDropShadowFlag = false;
      setDropShadow($window);
    }
  });
  $navbarVerticalCollapse.on('hide.bs.collapse', () => {
    if ($navbarVerticalCollapse.hasClass('show') && $window.width() < breakPoint) {
      navDropShadowFlag = false;
    } else {
      navDropShadowFlag = true;
    }
    setDropShadow($window);
  });
});
