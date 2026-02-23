document.addEventListener("DOMContentLoaded", () => {
  // Right sidebar TOC root <ul>
  const tocRoot = document.querySelector(".bd-toc nav ul, .bd-toc .tocsection nav ul");
  if (!tocRoot) return;

  // Find the <li> for the currently active heading
  // (pydata/sbt mark the current <a> with `.current` at various times)
  const currentLink =
    tocRoot.querySelector("a.current") ||
    tocRoot.querySelector("li.current > a") ||
    tocRoot.querySelector("li > a[aria-current='true']");
  if (!currentLink) return;

  const currentLi = currentLink.closest("li");
  if (!currentLi) return;

  // Helper: get the top-level <li> ancestor (child of tocRoot)
  const topLiOf = (li) => {
    let node = li;
    while (node && node.parentElement !== tocRoot) {
      node = node.parentElement.closest("li");
    }
    return node;
  };

  const activeTop = topLiOf(currentLi);

  // 1) Hide every top-level subsection except the active one
  tocRoot.querySelectorAll(":scope > li").forEach((li) => {
    if (li !== activeTop) {
      li.style.display = "none";
    }
  });

  // 2) Within the active branch, ensure all descendants are visible
  //    (pydata uses nested <ul>; sometimes hidden via CSS or collapsed state)
  const showBranch = (li) => {
    // show this li and all nested uls/lis
    li.style.display = "";
    li.querySelectorAll("ul, li").forEach((el) => {
      el.style.display = "";
    });
  };
  showBranch(activeTop);

  // 3) Optionally, hide siblings at deeper nesting levels too,
  //    so only the path-to-current + its descendants remain
  let ancestor = currentLi;
  while (ancestor && ancestor !== activeTop.parentElement) {
    const parentUl = ancestor.closest("ul");
    if (!parentUl || parentUl === tocRoot) break;
    parentUl.querySelectorAll(":scope > li").forEach((sib) => {
      // keep the ancestor chain visible; hide its siblings
      if (sib !== ancestor) sib.style.display = "none";
    });
    ancestor = parentUl.closest("li");
  }
});
