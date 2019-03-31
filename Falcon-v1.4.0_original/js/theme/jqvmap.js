/*-----------------------------------------------
|   jqvmap
-----------------------------------------------*/
/*-----------------------------------------------
|   Get color
-----------------------------------------------*/
const percentColors = [
  { pct: 0.0, color: { r: 0xde, g: 0xec, b: 0xfc } },
  { pct: 0.05, color: { r: 0x77, g: 0xb2, b: 0xf2 } },
  { pct: 0.1, color: { r: 0x0c, g: 0x63, b: 0xbd } },
];

const getColorForPercentage = (pct) => {
  let i = 1;
  for (i; i < percentColors.length - 1; i += 1) {
    if (pct < percentColors[i].pct) {
      break;
    }
  }
  const lower = percentColors[i - 1];
  const upper = percentColors[i];
  const range = upper.pct - lower.pct;
  const rangePct = (pct - lower.pct) / range;
  const pctLower = 1 - rangePct;
  const pctUpper = rangePct;
  const color = {
    r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
    g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
    b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper),
  };
  return `rgb(${color.r}, ${color.g}, ${color.b})`;
};

window.utils.$document.ready(() => {
  const getA = (n, interval = 1, initial = 1) => initial + (n - 1) * interval;
  const getCommonDifference = (S, a, n) => (2 * (S - (a * n))) / (n * (n - 1));

  const interval = getCommonDifference(100, 1, 20);
  const countries = {
    us: Math.floor(getA(20, interval) * 1618),
    cn: Math.floor(getA(19, interval) * 1618),
    jp: Math.floor(getA(18, interval) * 1618),
    de: Math.floor(getA(17, interval) * 1618),
    gb: Math.floor(getA(16, interval) * 1618),
    fr: Math.floor(getA(15, interval) * 1618),
    in: Math.floor(getA(14, interval) * 1618),
    it: Math.floor(getA(13, interval) * 1618),
    br: Math.floor(getA(12, interval) * 1618),
    ca: Math.floor(getA(11, interval) * 1618),
    ru: Math.floor(getA(10, interval) * 1618),
    kr: Math.floor(getA(9, interval) * 1618),
    es: Math.floor(getA(8, interval) * 1618),
    au: Math.floor(getA(7, interval) * 1618),
    mx: Math.floor(getA(6, interval) * 1618),
    id: Math.floor(getA(5, interval) * 1618),
    nl: Math.floor(getA(4, interval) * 1618),
    tr: Math.floor(getA(3, interval) * 1618),
    sa: Math.floor(getA(2, interval) * 1618),
    ch: Math.floor(getA(1, interval) * 1618),
    za: Math.floor(getA(14, interval) * 1618),
  };
  const getSum = array => array.reduce((a, b) => a + b, 0);
  const getColors = () => {
    const colors = {};
    const countriesValues = Object.keys(countries).map(country => countries[country]);
    Object
      .keys(countries)
      .map((country) => {
        const ratio = countries[country] / getSum(countriesValues);
        colors[country] = getColorForPercentage(ratio);
        return false;
      });
    return colors;
  };

  /*-----------------------------------------------
  |   Map size
  -----------------------------------------------*/
  const setMapSize = (map) => {
    const containerWidth = map.parent().width();
    const containerHeight = (containerWidth / 1.618);
    map.css({ width: containerWidth, height: containerHeight });
  };
  const vmaps = $('.vmap');
  vmaps.length && vmaps.each((index, value) => {
    const $this = $(value);
    const options = $.extend({
      map: 'world_en',
      backgroundColor: '#ffffff',
      borderColor: '#d8e2ef',
      borderOpacity: 1,
      borderWidth: 1,
      color: '#d8e2ef',
      colors: getColors(),
      onLabelShow(event, label, code) {
        /* eslint-disable */
        if (Object.keys(countries).indexOf(code) >= 0) {
          label[0].innerHTML = `<strong>${label[0].innerHTML}</strong><br />Active user: ${countries[code]}`;
        } else {
          label[0].innerHTML = `<strong>${label[0].innerHTML}</strong><br />Active user: 0`;
        }
        /* eslint-enable */
      },
      enableZoom: false,
      hoverColor: '#39afd1',
      hoverOpacity: 0.5,
      normalizeFunction: 'linear',
      selectedColor: '#e63757',
      selectedRegions: null,
      showTooltip: true,
      onResize() {
        setMapSize($this);
      },
    }, $this.data('options'));
    setMapSize($this);
    $this.vectorMap(options);
  });
});
