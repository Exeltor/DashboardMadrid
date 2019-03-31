'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Tabs
-----------------------------------------------*/
utils.$document.ready(() => {
  const $fancyTabs = $('.fancy-tab');
  if ($fancyTabs.length) {
    const Selector = {
      TAB_BAR: '.nav-bar',
      TAB_BAR_ITEM: '.nav-bar-item',
      TAB_CONTENTS: '.tab-contents',
    };
    const ClassName = {
      ACTIVE: 'active',
      TRANSITION_REVERSE: 'transition-reverse',
      TAB_INDICATOR: 'tab-indicator',
    };
    /*-----------------------------------------------
    |   Function for active tab indicator change
    -----------------------------------------------*/
    const updateIncicator = ($indicator, $tabs, $tabnavCurrentItem) => {
      const { left } = $tabnavCurrentItem.position();
      const right = $tabs
        .children(Selector.TAB_BAR).outerWidth() - (left + $tabnavCurrentItem.outerWidth());
      $indicator.css({ left, right });
    };

    $fancyTabs.each((index, value) => {
      const $tabs = $(value);
      const $navBar = $tabs.children(Selector.TAB_BAR);
      let $tabnavCurrentItem = $navBar.children(`${Selector.TAB_BAR_ITEM}.${ClassName.ACTIVE}`);
      $navBar.append(`
        <div class=${ClassName.TAB_INDICATOR}></div>
      `);
      const $indicator = $navBar.children(`.${ClassName.TAB_INDICATOR}`);
      let $preIndex = $tabnavCurrentItem.index();
      updateIncicator($indicator, $tabs, $tabnavCurrentItem);

      $navBar.children(Selector.TAB_BAR_ITEM).click((e) => {
        $tabnavCurrentItem = $(e.currentTarget);

        const $currentIndex = $tabnavCurrentItem.index();
        const $tabContent = $tabs.children(Selector.TAB_CONTENTS).children().eq($currentIndex);

        $tabnavCurrentItem.siblings().removeClass(ClassName.ACTIVE);
        $tabnavCurrentItem.addClass(ClassName.ACTIVE);
        $tabContent.siblings().removeClass(ClassName.ACTIVE);
        $tabContent.addClass(ClassName.ACTIVE);

        /*-----------------------------------------------
        |   Indicator Transition
        -----------------------------------------------*/
        updateIncicator($indicator, $tabs, $tabnavCurrentItem);
        if (($currentIndex - $preIndex) <= 0) {
          $indicator.addClass(ClassName.TRANSITION_REVERSE);
        } else {
          $indicator.removeClass(ClassName.TRANSITION_REVERSE);
        }
        $preIndex = $currentIndex;
      });
      utils.$window.on('resize', () => {
        updateIncicator($indicator, $tabs, $tabnavCurrentItem);
      });
    });
  }
});
