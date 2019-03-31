/*-----------------------------------------------
|   Flatpickr
-----------------------------------------------*/
window.utils.$document.ready(() => {
  const select2 = $('.selectpicker');
  select2.length && select2.each((index, value) => {
    const $this = $(value);
    const options = $.extend({},$this.data('options'));
    $this.select2(options);
  });
});

window.utils.$document.ready(() => {
  const datetimepicker = $('.datetimepicker');
  datetimepicker.length && datetimepicker.each((index, value) => {
    const $this = $(value);
    const options = $.extend({dateFormat: 'd/m/y'}, $this.data('options'));
    $this.attr('placeholder', options.dateFormat);
    $this.flatpickr(options);
  });
});
