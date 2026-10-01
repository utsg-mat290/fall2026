MAT290H1F - Advanced Engineering Mathematics - Fall 2026
=====================================================

This package follows the supplied CSC358 Winter 2025 course-page format:
R Markdown sources, a navy navigation bar, burgundy headings, a pale logistics
section, an instructor photograph and a lecture schedule table. The course
illustration is a small SVG of the complex unit circle. The mobile layout
turns each schedule row into a labelled block.

OPEN THE WEBSITE

Open docs/index.html in your browser. All presentation assets are local.
The course page, syllabus summary and schedule PDF work without a build step.
External university pages and Quercus still require internet access; Quercus
materials may also require course enrolment.

PUBLISH WITH GITHUB PAGES

Option A - a separate course repository, like your previous course sites:
1. Copy the contents of MAT290-Fall2026 into your course repository.
2. Commit and push these files, including docs/.
3. In the repository's Pages settings, publish your chosen branch's /docs
   folder using the branch publishing option.
4. Use the website URL shown by GitHub after deployment finishes.

Option B - within your existing erfanmeskar.github.io website:
1. Copy the CONTENTS of this package's docs/ folder into mat290/fall2026/
   inside the directory that your existing website publishes or builds from.
   Do not replace your existing docs/index.html with the course homepage.
2. If your personal site uses Jekyll, put mat290/fall2026/ in the Jekyll source
   directory and let the existing build copy these static files to its output.
   Do not move .nojekyll to your personal site's root.
3. Add the entry in personal-site-teaching-entry.txt to _pages/teaching.md,
   then rebuild/publish your personal site using its usual workflow.
4. The relative course address is /mat290/fall2026/.

This package has not been pushed to GitHub or published. No repository access
or deployment configuration was supplied.

The separate MAT290-Fall2026-preview.html file is a self-contained preview:
it embeds the styles, images, schedule PDF and supplied lecture 9 worksheet,
with the syllabus summary appended on the same page. The other worksheet
links target PDFs to be added. Use docs/ in this package for publishing.

EDIT AND REBUILD

Edit these files:
  index.rmd         Course information and all 12 groups of three lectures.
  syllabus.rmd      Short policy summary and official-syllabus link.
  _site.yml         Navigation and R Markdown site settings.
  css/style.css     Course styling and responsive schedule rules.
  js/worksheet-availability.js  Checks worksheet windows when links are clicked.

RStudio / R Markdown (the same source workflow as your previous course):
  rmarkdown::render_site()

Run from the MAT290-Fall2026 directory. The rmarkdown package is needed;
RStudio normally supplies Pandoc. Commit the updated docs/ after rendering.

Alternative, without R (Python 3, Pandoc and PyYAML are required):
  python build.py

The included docs/ was generated with the Python/Pandoc option. The R Markdown
sources use plain Markdown and HTML without executable R chunks. The RStudio
rendering route has not been executed in this environment.

For a local web preview from the project directory:
  python -m http.server 8000 --directory docs
Then open http://localhost:8000/ in your browser.

SOURCE CHOICES AND DETAILS TO MAINTAIN

- Instructor and lecture section: Erfan Meskar, LEC0101 (shown as LEC101 in
  the official syllabus), Mon 5-6 PM, Wed 3-4 PM, Thu 5-6 PM, SF1101.
- The attached schedule is labelled LEC0102. It explicitly describes a
  tentative shared sequence with different possible paces across sections.
  Its lecture groupings, readings and every assigned problem are retained.
  Worksheet dates follow the instructor's specified calendar: first lecture
  Wednesday September 9; Monday 5-6 PM, Wednesday 3-4 PM, Thursday 5-6 PM;
  October 12, 26, 28 and 29 are omitted. Regular lectures end on Monday,
  December 7. Lecture 36 is a make-up on Tuesday, December 8, 5-6 PM.
- All homework refers to Zill's 7th edition. The final row of the supplied
  PDF is clipped visually; its text layer includes Section 19.6 problems
  21, 28, 31, 33, 35, which are included in the page.
- The main Quercus link is https://q.utoronto.ca/courses/469114, as supplied.
- The ODE and inverse-Laplace note links are the actual links embedded in
  the supplied LEC0102 schedule. Confirm your students can access them;
  otherwise replace them with the corresponding files in your section.
- Office hours and announcements point students to Quercus.
  No office-hour time, TA roster or final-exam date was invented.
- The Lecture Worksheet column contains three links per row, labelled
  ws-L01 through ws-L36. Their PDF paths are worksheet/ws-L01.pdf through
  worksheet/ws-L36.pdf. The supplied mat290-ws09.pdf is included as
  worksheet/ws-L09.pdf. The other 35 links are prepared for future PDFs and
  require those files before they can open during their lecture windows.
- Add the remaining PDFs to worksheet/ using those exact filenames, then
  rebuild and publish docs/. Existing worksheet links do not need editing.
- Each row has a Supplementary Material cell. In index.rmd, replace that
  cell's dash with links to videos or extra readings; for example:
  <a href="YOUR_VIDEO_URL">Stability example (video)</a>
  Separate multiple links with <br>, then rebuild.
- The five quiz dates and assessment information follow the official Fall
  2026 syllabus (last updated September 11, 2026). Room changes and the full
  policy wording remain linked to that official source.
- The final-exam threshold is reproduced as stated in that syllabus: under
  40% on the final means a course grade of 49%, regardless of the average.

WORKSHEET AVAILABILITY

Each worksheet link in index.rmd has data-available-from and data-available-until
attributes. The interval includes the opening instant and excludes the closing
instant: a 5-6 PM window opens at 5:00 PM and closes at exactly 6:00 PM.
Dates and times are also displayed below each worksheet link in the schedule.

The script in js/worksheet-availability.js runs on each click, keyboard
activation, Ctrl/Cmd-click and middle-click. Outside the assigned interval,
it prevents navigation and shows this exact message in a browser dialog:
The worksheet links are only available during their corresponding lecture

All timestamps use explicit UTC offsets for America/Toronto: -04:00 through
lecture 19 (October 22), and -05:00 beginning with lecture 20 (November 2).
This accounts for the November 1 clock change, and works when a student's
browser uses a different time zone. The check uses the student's device clock.

To reschedule a worksheet, edit its two data attributes in index.rmd, using the
correct date, local time and UTC offset; update its title and the displayed
<time> text/datetime to match. Rebuild and publish docs/. The JavaScript is
loaded by includes/footer.html in both the Python and R Markdown workflows.

This is browser-side link behaviour, not access control. The public PDF URLs
and public repository remain accessible directly. Downloads are not revoked.
The self-contained preview uses the same time checks as the publishable site.

LECTURE AND WORKSHEET WINDOWS - ALL TIMES IN TORONTO, 2026

Lecture  Worksheet  Day  Date          Available
-------  ---------  ---  ----------    ---------
      1  ws-L01     Wed  2026-09-09    3-4 PM EDT
      2  ws-L02     Thu  2026-09-10    5-6 PM EDT
      3  ws-L03     Mon  2026-09-14    5-6 PM EDT
      4  ws-L04     Wed  2026-09-16    3-4 PM EDT
      5  ws-L05     Thu  2026-09-17    5-6 PM EDT
      6  ws-L06     Mon  2026-09-21    5-6 PM EDT
      7  ws-L07     Wed  2026-09-23    3-4 PM EDT
      8  ws-L08     Thu  2026-09-24    5-6 PM EDT
      9  ws-L09     Mon  2026-09-28    5-6 PM EDT
     10  ws-L10     Wed  2026-09-30    3-4 PM EDT
     11  ws-L11     Thu  2026-10-01    5-6 PM EDT
     12  ws-L12     Mon  2026-10-05    5-6 PM EDT
     13  ws-L13     Wed  2026-10-07    3-4 PM EDT
     14  ws-L14     Thu  2026-10-08    5-6 PM EDT
     15  ws-L15     Wed  2026-10-14    3-4 PM EDT
     16  ws-L16     Thu  2026-10-15    5-6 PM EDT
     17  ws-L17     Mon  2026-10-19    5-6 PM EDT
     18  ws-L18     Wed  2026-10-21    3-4 PM EDT
     19  ws-L19     Thu  2026-10-22    5-6 PM EDT
     20  ws-L20     Mon  2026-11-02    5-6 PM EST
     21  ws-L21     Wed  2026-11-04    3-4 PM EST
     22  ws-L22     Thu  2026-11-05    5-6 PM EST
     23  ws-L23     Mon  2026-11-09    5-6 PM EST
     24  ws-L24     Wed  2026-11-11    3-4 PM EST
     25  ws-L25     Thu  2026-11-12    5-6 PM EST
     26  ws-L26     Mon  2026-11-16    5-6 PM EST
     27  ws-L27     Wed  2026-11-18    3-4 PM EST
     28  ws-L28     Thu  2026-11-19    5-6 PM EST
     29  ws-L29     Mon  2026-11-23    5-6 PM EST
     30  ws-L30     Wed  2026-11-25    3-4 PM EST
     31  ws-L31     Thu  2026-11-26    5-6 PM EST
     32  ws-L32     Mon  2026-11-30    5-6 PM EST
     33  ws-L33     Wed  2026-12-02    3-4 PM EST
     34  ws-L34     Thu  2026-12-03    5-6 PM EST
     35  ws-L35     Mon  2026-12-07    5-6 PM EST
     36  ws-L36     Tue  2026-12-08    5-6 PM EST (make-up lecture)

No lectures on October 12 (holiday) or October 26, 28 and 29 (reading week).
The 35 regular lectures run through December 7; the 36th is on December 8.

SOURCES

Official syllabus supplied by the instructor:
https://www.control.utoronto.ca/~maggiore/MAT290F.php
Accessible indexed version of the same university page:
https://www.control.utoronto.ca/people/profs/maggiore/MAT290F.php
(Fall 2026 version, last updated September 11, 2026; consulted September 30.)
Direct retrieval returned Site Unavailable here; the university page's full
indexed text supplied the syllabus information. The page links use the
canonical address, while this file retains the originally supplied address.

Attached shared schedule:
Course Schedule_ MAT290H1 F LEC0102 20269_Advanced Engineering Mathematics.pdf
A byte-for-byte copy is in files/MAT290-Fall2026-Course-Schedule.pdf.

Template and instructor photograph:
webpages.zip -> csc358/spring2025/
Personal-site link format:
webpages.zip -> personal/erfanmeskar.github.io/_pages/teaching.md

Bundled third-party libraries are documented in THIRD-PARTY-NOTICES.txt.

VALIDATION

The prebuilt HTML was compiled successfully, all local links and anchors were
checked, and the 12 lecture groups cover lectures 1-36. Every numerical token
in the homework column was compared with the corresponding PDF column and
matched. Desktop and mobile layouts were reviewed with an offline renderer.
Live browser preview was unavailable in this environment, so browser menu
interaction has not been exercised here.

The worksheet calendar was checked against all 36 dates in the instructor's
weekly pattern, including the October 12 holiday, October 26/28/29 reading
week, December 8 make-up lecture and the November clock change. The deployed JavaScript passed simulated click, keyboard, modified
click and middle-click checks before, at, during and after every lecture
window. These checks used Node; live browser interaction was not available.

GitHub Pages publishing documentation:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
