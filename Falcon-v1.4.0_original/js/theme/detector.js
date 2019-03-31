'use strict';

import utils from './Utils';

/*-----------------------------------------------
|   Variables
-----------------------------------------------*/
/*
  global opr, safari
*/

/*-----------------------------------------------
|   Detector
-----------------------------------------------*/
const spDetector = (() => {
  const Detector = {
    isMobile: /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(utils.nua),
    isOSX: utils.nua.match(/(iPad|iPhone|iPod|Macintosh)/g),
    isOpera: (!!window.opr && !!opr.addons) || !!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0,
    isFirefox: typeof InstallTrigger !== 'undefined',
    isSafari: /constructor/i.test(window.HTMLElement) || (p => p.toString() === '[object SafariRemoteNotification]')(!window.safari || safari.pushNotification),
    isNewerIE: utils.nua.match(/msie (9|([1-9][0-9]))/i),
    isOlderIE: utils.nua.match(/msie/i) && !this.isNewerIE,
    isAncientIE: utils.nua.match(/msie 6/i),
    isIE: this.isAncientIE || this.isOlderIE || this.isNewerIE,
    isIE11: !!window.MSInputMethodContext && !!document.documentMode,
    isEdge: !this.isIE11 && !this.isIE && !!window.StyleMedia,
    isChrome: !!window.chrome && !!window.chrome.webstore,
    isBlink: (this.isChrome || this.isOpera) && !!window.CSS,
    isPuppeteer: utils.nua.match(/puppeteer/i),
    isIOS: parseFloat(((/CPU.*OS ([0-9_]{1,5})|(CPU like).*AppleWebKit.*Mobile/i.exec(utils.nua) || [0, ''])[1]).replace('undefined', '3_2').replace('_', '.').replace('_', '')) || false,
    iPadiPhoneFirefox: utils.nua.match(/iPod|iPad|iPhone/g) && utils.nua.match(/Gecko/g),
    macFirefox: utils.nua.match(/Macintosh/g) && utils.nua.match(/Gecko/g) && utils.nua.match(/rv:/g),
    isAndroid: (utils.nua.indexOf('Mozilla/5.0') > -1 && utils.nua.indexOf('Android ') > -1 && utils.nua.indexOf('AppleWebKit') > -1),
  };


  utils.$document.ready(() => {
    if (Detector.isOpera) utils.$html.addClass('opera');
    if (Detector.isMobile) utils.$html.addClass('mobile');
    if (Detector.isOSX) utils.$html.addClass('osx');
    if (Detector.isFirefox) utils.$html.addClass('firefox');
    if (Detector.isSafari) utils.$html.addClass('safari');
    if (Detector.isIOS) utils.$html.addClass('ios');
    if (Detector.isIE || Detector.isIE11) utils.$html.addClass('ie');
    if (Detector.isEdge) utils.$html.addClass('edge');
    if (Detector.isChrome) utils.$html.addClass('chrome');
    if (Detector.isBlink) utils.$html.addClass('blink');
    if (Detector.isPuppeteer) utils.$html.addClass('puppeteer');
  });

  return Detector;
})();

export default spDetector;

