/*-----------------------------------------------
|   Toastr
-----------------------------------------------*/
window.utils.$document.ready(() => {
  const $notifications = $('[data-notification]');
  $notifications.each((index, value) => {
    const { toastr } = window;
    const $this = $(value);
    const config = $this.data('notification');
    const defaultOptions = {
      closeButton: true,
      newestOnTop: false,
      positionClass: 'toast-bottom-right',
    };
    $this.on('click', () => {
      const { type, title, message } = config;
      const mergedOptions = $.extend(defaultOptions, config);
      toastr.options.positionClass !== mergedOptions.positionClass && toastr.remove();
      toastr.options = mergedOptions;
      switch (type) {
        case 'success':
          toastr.success(message, title);
          break;
        case 'warning':
          toastr.warning(message, title);
          break;
        case 'error':
          toastr.error(message, title);
          break;
        default:
          toastr.info(message, title);
          break;
      }
    });
  });
});
