'use strict';

/*-----------------------------------------------
|   Data table
-----------------------------------------------*/
window.utils.$document.ready(() => {
  const dataTables = $('.data-table');
  const customDataTable = (elem) => {
    elem.find('table').find('tfoot').addClass('bg-200');
    elem
      .find('.pagination')
      .addClass('pagination-sm')
      .closest('[class*="col"]')
      .removeClass('col-sm-12 col-md-7')
      .addClass('col-auto mt-2')
      .closest('.row')
      .addClass('no-gutters justify-content-center justify-content-md-between');
  };
  dataTables.length && dataTables.each((index, value) => {
    const $this = $(value);
    $this.DataTable({ responsive: true });
    const $wrpper = $this.closest('.dataTables_wrapper');
    customDataTable($wrpper);
    $this.on('draw.dt', () => customDataTable($wrpper));
  });
});
