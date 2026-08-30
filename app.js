/* =============================================================
   app.js — בונה את הגלריה מתוך data/videos.js, מפעיל מסננים ונגן.
   בדרך כלל אין צורך לגעת בקובץ הזה.
   ============================================================= */
(function () {
  "use strict";

  var ROLE_ORDER = ["כתיבה", "צילום", "עריכה"];

  var grid       = document.getElementById("grid");
  var gridEmpty  = document.getElementById("grid-empty");
  var filtersBox = document.getElementById("filters");
  var modal      = document.getElementById("modal");
  var player     = document.getElementById("modal-player");
  var modalTitle = document.getElementById("modal-title");
  var modalDesc  = document.getElementById("modal-desc");

  var videos = (typeof VIDEOS !== "undefined" && Array.isArray(VIDEOS)) ? VIDEOS : [];
  var activeFilter = "all";
  var lastFocused = null;

  /* ── עזרים ─────────────────────────────────────────────── */

  // מזהה YouTube תקין = בדיוק 11 תווים מהסט המותר
  function isRealId(id) {
    return typeof id === "string" && /^[A-Za-z0-9_-]{11}$/.test(id);
  }

  function pad(n) { return n < 10 ? "0" + n : String(n); }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  /* ── בניית כרטיס ───────────────────────────────────────── */

  function buildCard(video, index) {
    var card = el("article", "card");
    card.dataset.roles = (video.roles || []).join("|");

    /* מדיה */
    var media = el("div", "card__media");

    if (isRealId(video.youtubeId)) {
      var img = el("img", "card__thumb");
      img.loading = "lazy";
      img.decoding = "async";
      img.alt = "";                       // דקורטיבי — הכותרת ממילא בטקסט

      var hq = "https://i.ytimg.com/vi/" + video.youtubeId + "/hqdefault.jpg";
      var fellBack = false;

      function fallback() {
        if (fellBack) return;
        fellBack = true;
        img.src = hq;                     // hqdefault קיים תמיד
      }

      // לא לכל סרטון יש maxresdefault. כשאין — YouTube לא מחזיר שגיאה
      // אלא תמונה אפורה זעירה (120×90) עם סטטוס 200, ולכן בדיקת onerror
      // לבדה לא מספיקה וצריך לבדוק גם את הרוחב בפועל.
      img.addEventListener("load", function () {
        if (!fellBack && img.naturalWidth > 0 && img.naturalWidth < 200) fallback();
      });
      img.addEventListener("error", fallback);

      img.src = "https://i.ytimg.com/vi/" + video.youtubeId + "/maxresdefault.jpg";
      media.appendChild(img);
    } else {
      var ph = el("div", "card__placeholder");
      ph.appendChild(el("strong", null, pad(index + 1)));
      ph.appendChild(el("span", null, "ממתין למזהה סרטון"));
      media.appendChild(ph);
    }

    media.appendChild(el("span", "card__play"));
    card.appendChild(media);

    /* טקסט */
    card.appendChild(el("p", "card__index", "עבודה " + pad(index + 1)));
    card.appendChild(el("h3", "card__title", video.title || "ללא כותרת"));

    if (video.description) card.appendChild(el("p", "card__desc", video.description));
    if (video.context)     card.appendChild(el("p", "card__context", video.context));

    if (video.roles && video.roles.length) {
      var ul = el("ul", "card__roles");
      video.roles.forEach(function (role) { ul.appendChild(el("li", null, role)); });
      card.appendChild(ul);
    }

    /* שכבת הלחיצה */
    var hit = el("button", "card__hit");
    hit.type = "button";
    hit.setAttribute("aria-label", "צפייה בסרטון: " + (video.title || "ללא כותרת"));
    hit.addEventListener("click", function () { openModal(video, hit); });
    card.appendChild(hit);

    return card;
  }

  /* ── רינדור הגלריה ─────────────────────────────────────── */

  function render() {
    grid.textContent = "";
    var shown = 0;

    videos.forEach(function (video, i) {
      var roles = video.roles || [];
      if (activeFilter !== "all" && roles.indexOf(activeFilter) === -1) return;
      grid.appendChild(buildCard(video, i));
      shown++;
    });

    gridEmpty.hidden = shown > 0;
    observeReveals();
  }

  /* ── מסננים ────────────────────────────────────────────── */

  function buildFilters() {
    var present = ROLE_ORDER.filter(function (role) {
      return videos.some(function (v) { return (v.roles || []).indexOf(role) !== -1; });
    });

    // פחות משני תפקידים שונים — אין טעם במסנן
    if (present.length < 2) return;

    ["all"].concat(present).forEach(function (value) {
      var btn = el("button", "filter", value === "all" ? "הכל" : value);
      btn.type = "button";
      btn.setAttribute("aria-pressed", String(value === activeFilter));
      btn.addEventListener("click", function () {
        activeFilter = value;
        Array.prototype.forEach.call(filtersBox.children, function (b) {
          b.setAttribute("aria-pressed", String(b === btn));
        });
        render();
      });
      filtersBox.appendChild(btn);
    });
  }

  /* ── מודאל הנגן ────────────────────────────────────────── */

  function openModal(video, trigger) {
    lastFocused = trigger || document.activeElement;
    player.textContent = "";

    if (isRealId(video.youtubeId)) {
      var iframe = document.createElement("iframe");
      iframe.src =
        "https://www.youtube-nocookie.com/embed/" + video.youtubeId +
        "?autoplay=1&rel=0&modestbranding=1&playsinline=1&hl=he";
      iframe.title = video.title || "נגן וידאו";
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
      iframe.allowFullscreen = true;
      iframe.referrerPolicy = "strict-origin-when-cross-origin";
      player.appendChild(iframe);
    } else {
      var notice = el("div", "modal__notice");
      notice.appendChild(el("p", null, "עדיין לא הוזן מזהה YouTube לסרטון הזה."));
      var line = el("p");
      line.appendChild(document.createTextNode("מעדכנים את השדה "));
      line.appendChild(el("code", null, "youtubeId"));
      line.appendChild(document.createTextNode(" בקובץ "));
      line.appendChild(el("code", null, "data/videos.js"));
      notice.appendChild(line);
      player.appendChild(notice);
    }

    modalTitle.textContent = video.title || "";
    modalDesc.textContent  = [video.description, video.context].filter(Boolean).join(" · ");

    modal.hidden = false;
    document.body.classList.add("is-locked");
    modal.querySelector(".modal__close").focus();
  }

  function closeModal() {
    if (modal.hidden) return;
    modal.hidden = true;
    player.textContent = "";                 // עוצר את הניגון
    document.body.classList.remove("is-locked");
    if (lastFocused && lastFocused.isConnected) lastFocused.focus();
  }

  modal.addEventListener("click", function (e) {
    if (e.target.hasAttribute("data-close")) closeModal();
  });

  document.addEventListener("keydown", function (e) {
    if (modal.hidden) return;
    if (e.key === "Escape") { closeModal(); return; }

    // מלכודת פוקוס — Tab לא יוצא מהמודאל
    if (e.key === "Tab") {
      var focusables = modal.querySelectorAll("button, iframe, a[href]");
      if (!focusables.length) return;
      var first = focusables[0];
      var last  = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* ── אנימציית כניסה ────────────────────────────────────── */

  var io = ("IntersectionObserver" in window)
    ? new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -40px" })
    : null;

  function observeReveals() {
    var items = document.querySelectorAll(".reveal:not(.is-in), .card:not(.is-in)");
    Array.prototype.forEach.call(items, function (item, i) {
      item.classList.add("reveal");
      item.style.transitionDelay = Math.min(i, 5) * 60 + "ms";
      if (io) io.observe(item); else item.classList.add("is-in");
    });
  }

  // רשת ביטחון: אם מסיבה כלשהי ה-observer לא הופעל, מציגים הכל בכל מקרה.
  // עדיף אתר בלי אנימציה מאשר אתר ריק.
  function revealAllFallback() {
    var stuck = document.querySelectorAll(".reveal:not(.is-in)");
    Array.prototype.forEach.call(stuck, function (item) {
      var box = item.getBoundingClientRect();
      if (box.top < window.innerHeight * 1.1) item.classList.add("is-in");
    });
  }

  /* ── הפעלה ─────────────────────────────────────────────── */

  document.getElementById("year").textContent = new Date().getFullYear();
  buildFilters();
  render();
  observeReveals();

  // ההירו נחשף מיד, בלי להמתין לגלילה
  requestAnimationFrame(function () {
    var hero = document.querySelectorAll(".hero .reveal");
    Array.prototype.forEach.call(hero, function (item) { item.classList.add("is-in"); });
  });

  setTimeout(revealAllFallback, 1200);
  window.addEventListener("load", revealAllFallback);
})();
