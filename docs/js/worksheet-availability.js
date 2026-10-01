/* Worksheet dates are specified on the links in index.rmd.
 * Explicit UTC offsets preserve Toronto lecture times across the November
 * clock change, regardless of the visitor's own time zone.
 * This controls link clicks; PDFs on GitHub Pages remain publicly accessible.
 */
(function () {
  'use strict';

  var message = 'The worksheet links are only available during their corresponding lecture';

  function checkWorksheetWindow(event) {
    // Right-click is a context-menu action, not a request to open a worksheet.
    if (event.type === 'auxclick' && event.button !== 1) return;

    var target = event.target;
    var link = target && target.closest ? target.closest('a.worksheet-link') : null;
    if (!link) return;

    var opens = Date.parse(link.getAttribute('data-available-from'));
    var closes = Date.parse(link.getAttribute('data-available-until'));
    // Check on every activation, even if the page has been open for hours.
    // Include the opening instant; exclude the closing instant.
    var now = Date.now();
    if (Number.isFinite(opens) && Number.isFinite(closes) &&
        opens <= now && now < closes) return;

    event.preventDefault();
    window.alert(message);
  }

  // A keyboard activation and Ctrl/Cmd-click both dispatch a click event.
  document.addEventListener('click', checkWorksheetWindow, true);
  document.addEventListener('auxclick', checkWorksheetWindow, true);
})();
