(function(global2, factory) {
  typeof exports === "object" && typeof module !== "undefined" ? factory(exports, require("react")) : typeof define === "function" && define.amd ? define(["exports", "react"], factory) : (global2 = typeof globalThis !== "undefined" ? globalThis : global2 || self, factory(global2.Fy24HeaderCategories = {}, global2.React));
})(this, function(exports2, React) {
  "use strict";var __defProp = Object.defineProperty;
var __defProps = Object.defineProperties;
var __getOwnPropDescs = Object.getOwnPropertyDescriptors;
var __getOwnPropSymbols = Object.getOwnPropertySymbols;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __propIsEnum = Object.prototype.propertyIsEnumerable;
var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
var __spreadValues = (a, b) => {
  for (var prop in b || (b = {}))
    if (__hasOwnProp.call(b, prop))
      __defNormalProp(a, prop, b[prop]);
  if (__getOwnPropSymbols)
    for (var prop of __getOwnPropSymbols(b)) {
      if (__propIsEnum.call(b, prop))
        __defNormalProp(a, prop, b[prop]);
    }
  return a;
};
var __spreadProps = (a, b) => __defProps(a, __getOwnPropDescs(b));
var __async = (__this, __arguments, generator) => {
  return new Promise((resolve, reject) => {
    var fulfilled = (value) => {
      try {
        step(generator.next(value));
      } catch (e) {
        reject(e);
      }
    };
    var rejected = (value) => {
      try {
        step(generator.throw(value));
      } catch (e) {
        reject(e);
      }
    };
    var step = (x) => x.done ? resolve(x.value) : Promise.resolve(x.value).then(fulfilled, rejected);
    step((generator = generator.apply(__this, __arguments)).next());
  });
};

  var commonjsGlobal = typeof globalThis !== "undefined" ? globalThis : typeof window !== "undefined" ? window : typeof global !== "undefined" ? global : typeof self !== "undefined" ? self : {};
  function getDefaultExportFromCjs(x) {
    return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, "default") ? x["default"] : x;
  }
  var classnames$1 = { exports: {} };
  /*!
  	Copyright (c) 2018 Jed Watson.
  	Licensed under the MIT License (MIT), see
  	http://jedwatson.github.io/classnames
  */
  (function(module2) {
    (function() {
      var hasOwn = {}.hasOwnProperty;
      function classNames() {
        var classes = "";
        for (var i = 0; i < arguments.length; i++) {
          var arg = arguments[i];
          if (arg) {
            classes = appendClass(classes, parseValue(arg));
          }
        }
        return classes;
      }
      function parseValue(arg) {
        if (typeof arg === "string" || typeof arg === "number") {
          return arg;
        }
        if (typeof arg !== "object") {
          return "";
        }
        if (Array.isArray(arg)) {
          return classNames.apply(null, arg);
        }
        if (arg.toString !== Object.prototype.toString && !arg.toString.toString().includes("[native code]")) {
          return arg.toString();
        }
        var classes = "";
        for (var key in arg) {
          if (hasOwn.call(arg, key) && arg[key]) {
            classes = appendClass(classes, key);
          }
        }
        return classes;
      }
      function appendClass(value, newClass) {
        if (!newClass) {
          return value;
        }
        if (value) {
          return value + " " + newClass;
        }
        return value + newClass;
      }
      if (module2.exports) {
        classNames.default = classNames;
        module2.exports = classNames;
      } else {
        window.classNames = classNames;
      }
    })();
  })(classnames$1);
  var classnamesExports = classnames$1.exports;
  const classnames = /* @__PURE__ */ getDefaultExportFromCjs(classnamesExports);
  var transformAssetsDomain = function(url) {
    if (!url) {
      return url;
    }
    var finalUrl = url.replace(/sc0(\d)\.alicdn\.com/, "s.alicdn.com/@sc0$1").replace(/img\.alicdn\.com/, "s.alicdn.com/@img").replace(/gw\.alicdn\.com/, "s.alicdn.com/@img").replace(/ossgw\.alicdn\.com/, "s.alicdn.com/@ossgw").replace(/g\.alicdn\.com/, "s.alicdn.com/@g");
    return finalUrl;
  };
  const VIEW_MORE = "https://s.alicdn.com/@img/imgextra/i2/O1CN015j2EYl1oJ1ldUovSw_!!6000000005203-55-tps-95-95.svg";
  const LEFT_ARROW = "https://s.alicdn.com/@img/imgextra/i4/O1CN01gG3oRq28RzrMxpytF_!!6000000007930-2-tps-40-40.png";
  const parseQuery = (queryString) => {
    const queryPairs = queryString.split("&");
    const result = {};
    for (const pair of queryPairs) {
      const [key, value] = pair.split("=");
      if (key && value) {
        result[key] = decodeURIComponent(value);
      }
    }
    return result;
  };
  const debounce = (fn, time, immediate) => {
    let timeoutId;
    const delay = time;
    return (...args) => {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
      timeoutId = setTimeout(() => {
        fn.apply(void 0, args);
        timeoutId = null;
      }, delay);
    };
  };
  var _process_versions, _process, _window;
  var isNode = (
    // process 在 webpack 构建时可能未引起未声明报错的异常，需要额外判断
    typeof process !== "undefined" && !!((_process = process) === null || _process === void 0 ? void 0 : (_process_versions = _process.versions) === null || _process_versions === void 0 ? void 0 : _process_versions.node) || typeof ((_window = window) === null || _window === void 0 ? void 0 : _window.__getComponentInNode) === "function"
  );
  var aplusManualDot = function(logkey) {
    var logtype = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : "EXP", params = arguments.length > 2 ? arguments[2] : void 0, disableEncode = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : false;
    var recordArr = [];
    Object.keys(params || {}).forEach(function(key) {
      var value = params[key];
      if (!(value === void 0 || value === null)) {
        var recordValue = disableEncode ? value : encodeURIComponent(value);
        recordArr.push("".concat(key, "=").concat(recordValue));
      }
    });
    var recordStr = recordArr.join("&");
    (window.goldlog_queue || (window.goldlog_queue = [])).push({
      action: "goldlog.record",
      arguments: [
        logkey,
        logtype,
        recordStr
      ]
    });
  };
  var isAutoDotInit = function(logkey) {
    var cacheKey = "APLUS_AUTO_LOG_".concat(logkey);
    if (window[cacheKey]) {
      return true;
    } else {
      window[cacheKey] = 1;
      return false;
    }
  };
  var aplusAutoDot = function() {
    var collectType = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : "EXP", collectOptions = arguments.length > 1 ? arguments[1] : void 0;
    var _collectOptions;
    if (isNode || !((_collectOptions = collectOptions) === null || _collectOptions === void 0 ? void 0 : _collectOptions.length)) {
      return;
    }
    var q = window.goldlog_queue || (window.goldlog_queue = []);
    collectOptions.forEach(function(collectOption) {
      var logkey = collectOption.logkey;
      if (logkey && !isAutoDotInit("".concat(logkey, "-").concat(collectType))) {
        q.push({
          action: "goldlog.appendMetaInfo",
          arguments: [
            "aplus-auto-".concat(collectType.toLowerCase()),
            [
              collectOption
            ]
          ]
        });
      }
    });
  };
  const LOG_KEY = "/sc.header_categories";
  const autoExp = () => {
    aplusAutoDot("EXP", [
      {
        logkey: `${LOG_KEY}`,
        cssSelector: `[data-dot-header-categories]`,
        method: "get",
        props: ["data-params"]
      }
    ]);
  };
  const manualClick = (dotParams) => {
    aplusManualDot(`${LOG_KEY}`, "CLK", dotParams);
  };
  const Level1Unit = (props) => {
    const { imageUrl, title, className, handleClick, dotParams = "" } = props;
    return /* @__PURE__ */ React.createElement(
      "div",
      {
        className: classnames("hc-level1-cate-unit", className),
        "data-level1-category-id": props.categoryId,
        "data-dot-header-categories": true,
        "data-params": `type=level1_category&level1CategoryId=${props.categoryId}&title=${props.titleEn || ""}&${dotParams}`,
        onClick: () => {
          handleClick && handleClick();
          manualClick(__spreadValues({
            type: "level1_category",
            level1CategoryId: props.categoryId,
            title: props.titleEn || ""
          }, parseQuery(dotParams)));
        }
      },
      /* @__PURE__ */ React.createElement(
        "div",
        {
          className: "img",
          style: {
            background: `url(${transformAssetsDomain(imageUrl)}) center center / contain no-repeat`
          }
        }
      ),
      /* @__PURE__ */ React.createElement("span", { className: "title" }, title)
    );
  };
  const Level1Panel = (props) => {
    const { categoryList = [], activeCategoryId, onCategoryClick, modalRef, rightPanelRef } = props;
    React.useEffect(() => {
      if ((modalRef == null ? void 0 : modalRef.current) && activeCategoryId) {
        const leftActiveItem = modalRef.current.querySelector(
          `[data-level1-category-id="${activeCategoryId}"]`
        );
        if (leftActiveItem) {
          leftActiveItem.scrollIntoView({ behavior: "auto", block: "start" });
        }
      }
      if (rightPanelRef == null ? void 0 : rightPanelRef.current) {
        const targetItem = rightPanelRef.current.querySelector(
          `[data-category-id="${activeCategoryId}"]`
        );
        if (targetItem) {
          targetItem.scrollIntoView({ behavior: "auto", block: "start" });
        }
      }
    }, []);
    return /* @__PURE__ */ React.createElement(
      "div",
      {
        className: classnames("hc-level1-panel"),
        "data-dot-header-categories": true,
        "data-params": "type=modal_level1_panel&action=category-panel"
      },
      /* @__PURE__ */ React.createElement("div", { className: "level1-panel-list" }, categoryList == null ? void 0 : categoryList.map((category) => {
        return /* @__PURE__ */ React.createElement(
          Level1Unit,
          {
            key: `left-${category.categoryId}`,
            dotParams: "position=modal_panel",
            categoryId: category.categoryId,
            imageUrl: category.imageUrl,
            title: category.title,
            className: classnames({ active: category.categoryId === activeCategoryId }),
            handleClick: () => onCategoryClick(category.categoryId)
          }
        );
      }))
    );
  };
  const Level3CategoryItem = (props) => {
    const { imageUrl, action, className, icon, title, handleClick, dotParams = "" } = props;
    return (
      // eslint-disable-next-line react/jsx-no-target-blank
      /* @__PURE__ */ React.createElement(
        "a",
        {
          className: classnames("hc-leaf-item", className),
          href: action || void 0,
          target: "_blank",
          "data-dot-header-categories": true,
          "data-params": `type=leaf_category&leafCategoryId=${props.categoryId || ""}&title=${props.titleEn || ""}&${dotParams}`,
          onClick: (e) => {
            e.stopPropagation();
            handleClick && handleClick();
            manualClick(__spreadValues({
              type: "leaf_category",
              leafCategoryId: props.categoryId || "",
              title: props.titleEn || ""
            }, parseQuery(dotParams)));
          }
        },
        /* @__PURE__ */ React.createElement("div", { className: "product-wrapper" }, /* @__PURE__ */ React.createElement("img", { src: transformAssetsDomain(imageUrl), className: "product-img", loading: "lazy" })),
        icon && /* @__PURE__ */ React.createElement("img", { src: transformAssetsDomain(icon), className: "icon", loading: "lazy" }),
        /* @__PURE__ */ React.createElement("div", { className: "title" }, title)
      )
    );
  };
  const Level3Unit = (props) => {
    var _a;
    const {
      category,
      className,
      type = "category",
      viewAllText = "View all",
      dotParams = "",
      categoryEntryText = "",
      handleViewMoreClick
    } = props;
    const maxItems = type === "leaf" ? 13 : 14;
    const filteredItems = (category.leaves || []).filter((leaf) => leaf == null ? void 0 : leaf.imageUrl);
    const items = filteredItems.slice(0, maxItems) || [];
    const isLeaf = type === "leaf";
    const itemCount = items.length;
    const showOnlyViewMore = isLeaf && itemCount === 0;
    const categoryLink = (category == null ? void 0 : category.categoryLink) || "";
    const shouldApplyFirstRowLessLeaves = () => {
      const isSpecialCase = itemCount === 6 && isLeaf;
      const isLessThanOrEqualToSeven = itemCount <= 7 && !isSpecialCase;
      const isIncompleteSecondRow = itemCount > 7 && itemCount < maxItems;
      return isLessThanOrEqualToSeven || isIncompleteSecondRow;
    };
    const shouldApplySecondRowLessLeaves = () => {
      const isExactlySeven = itemCount === 7;
      const isLessThanSix = itemCount < 6;
      const isIncompleteSecondRow = itemCount > 7 && itemCount < maxItems;
      return isExactlySeven || isLessThanSix || isIncompleteSecondRow;
    };
    const createCategoryItem = (leaf, key) => /* @__PURE__ */ React.createElement(
      Level3CategoryItem,
      {
        icon: leaf == null ? void 0 : leaf.icon,
        key: `leaf-${leaf == null ? void 0 : leaf.categoryId}`,
        imageUrl: leaf.imageUrl,
        action: leaf.action,
        dotParams,
        categoryId: leaf.categoryId,
        title: leaf.title
      }
    );
    const createViewMoreItem = (key) => /* @__PURE__ */ React.createElement(
      Level3CategoryItem,
      {
        dotParams: "action=more&position=modal_panel",
        imageUrl: VIEW_MORE,
        key: `${category.categoryId}-view-more`,
        title: viewAllText,
        handleClick: handleViewMoreClick
      }
    );
    const createEmptyItem = (key) => /* @__PURE__ */ React.createElement("div", { key, className: "leaf-item-empty" });
    const mapItemsWithEmpty = (itemList, startIdx = 0) => itemList.map(
      (leaf, idx) => (leaf == null ? void 0 : leaf.imageUrl) ? createCategoryItem(leaf) : createEmptyItem(`leaf-empty-${startIdx + idx}`)
    );
    const renderFirstRow = () => {
      if (showOnlyViewMore) {
        return [createViewMoreItem()];
      }
      if (itemCount <= 7) {
        if (itemCount === 6 && type === "leaf") {
          const firstRowItems = items.map((leaf) => createCategoryItem(leaf));
          firstRowItems.push(createViewMoreItem());
          return firstRowItems.reverse();
        }
        if (type === "leaf") {
          return mapItemsWithEmpty(items).concat(createViewMoreItem()).concat(
            Array(7 - itemCount).fill(null).map((_, idx) => createEmptyItem(`leaf-empty-${idx}`))
          ).slice(0, 7);
        } else {
          return mapItemsWithEmpty(items).concat(
            Array(7 - itemCount).fill(null).map((_, idx) => createEmptyItem(`leaf-empty-${idx}`))
          ).slice(0, 7);
        }
      }
      return items.slice(0, 7).reverse().map((leaf) => createCategoryItem(leaf));
    };
    const renderSecondRow = () => {
      if (showOnlyViewMore) {
        return null;
      }
      if (itemCount < 7) {
        return null;
      }
      if (type !== "leaf") {
        if (itemCount === 7) {
          return null;
        } else {
          return items.concat(Array(7).fill(null)).slice(7, 14).map(
            (leaf, idx) => (leaf == null ? void 0 : leaf.imageUrl) ? createCategoryItem(leaf) : createEmptyItem(`leaf-empty-${idx}`)
          );
        }
      } else {
        if (itemCount === 7) {
          return [createViewMoreItem()];
        }
        if (itemCount >= 7 && itemCount < 13) {
          const secondRowItems = items.slice(7, itemCount).map((leaf) => createCategoryItem(leaf));
          secondRowItems.push(createViewMoreItem());
          secondRowItems.push(
            ...Array(14 - itemCount).fill(null).map((_, idx) => createEmptyItem(`leaf-empty-${idx}`))
          );
          return secondRowItems.slice(0, 7);
        } else {
          return items.slice(7, maxItems).map((leaf) => createCategoryItem(leaf)).concat(createViewMoreItem()).reverse();
        }
      }
    };
    return /* @__PURE__ */ React.createElement(
      "div",
      {
        className: classnames("hc-level3-cate-unit", className),
        "data-category-id": category.categoryId
      },
      /* @__PURE__ */ React.createElement("div", { className: "category-title-container" }, /* @__PURE__ */ React.createElement("div", { className: "category-title" }, category.title), categoryLink && /* @__PURE__ */ React.createElement(
        "a",
        {
          className: "category-link",
          href: categoryLink || void 0,
          target: "_blank",
          "data-dot-header-categories": true,
          "data-params": `type=level1_category_link&categoryId=${category == null ? void 0 : category.categoryId}`
        },
        categoryEntryText
      )),
      !!((_a = category == null ? void 0 : category.leaves) == null ? void 0 : _a.length) && /* @__PURE__ */ React.createElement("div", { className: "leaf-container" }, /* @__PURE__ */ React.createElement(
        "div",
        {
          className: classnames("leaf-row", "first-row", {
            "less-leaves": shouldApplyFirstRowLessLeaves()
          })
        },
        renderFirstRow()
      ), /* @__PURE__ */ React.createElement(
        "div",
        {
          className: classnames("leaf-row", "second-row", {
            "less-leaves": shouldApplySecondRowLessLeaves()
          })
        },
        renderSecondRow()
      ))
    );
  };
  const Level2Unit = (props) => {
    const { title, className, handleClick } = props;
    return /* @__PURE__ */ React.createElement(
      "div",
      {
        className: classnames("hc-level2-cate-unit", className),
        "data-dot-header-categories": true,
        "data-params": `type=tree_panel_level2_cate&level2categoryId=${props.categoryId}&title=${props.titleEn || ""}`,
        onClick: () => {
          handleClick && handleClick();
          manualClick({
            type: "tree_panel_level2_cate",
            level2categoryId: props.categoryId,
            title: props.titleEn || ""
          });
        }
      },
      /* @__PURE__ */ React.createElement("span", { className: "title" }, title)
    );
  };
  var lib = {};
  Object.defineProperty(lib, "__esModule", { value: true });
  var transferDomain_1 = lib.transferDomain = void 0;
  function transferDomain(domain, customHost) {
    const host = customHost || location && location.hostname;
    if (host) {
      const suffixList = host.match(/alibaba\.(.*)/);
      if (suffixList && suffixList.length > 0) {
        return domain.replace("com", suffixList[1]);
      }
    }
    return domain;
  }
  transferDomain_1 = lib.transferDomain = transferDomain;
  var fetchJsonp$1 = { exports: {} };
  (function(module2, exports3) {
    (function(global2, factory) {
      {
        factory(exports3, module2);
      }
    })(commonjsGlobal, function(exports4, module3) {
      var defaultOptions = {
        timeout: 5e3,
        jsonpCallback: "callback"
      };
      function generateCallbackFunction() {
        return "jsonp_" + Date.now() + "_" + Math.ceil(Math.random() * 1e5);
      }
      function clearFunction(functionName) {
        try {
          delete window[functionName];
        } catch (e) {
          window[functionName] = void 0;
        }
      }
      function removeScript(scriptId) {
        var script = document.getElementById(scriptId);
        if (script) {
          document.getElementsByTagName("head")[0].removeChild(script);
        }
      }
      function fetchJsonp2(_url) {
        var options = arguments.length <= 1 || arguments[1] === void 0 ? {} : arguments[1];
        var url = _url;
        var timeout = options.timeout || defaultOptions.timeout;
        var jsonpCallback = options.jsonpCallback || defaultOptions.jsonpCallback;
        var timeoutId = void 0;
        return new Promise(function(resolve, reject) {
          var callbackFunction = options.jsonpCallbackFunction || generateCallbackFunction();
          var scriptId = jsonpCallback + "_" + callbackFunction;
          window[callbackFunction] = function(response) {
            resolve({
              ok: true,
              // keep consistent with fetch API
              json: function json() {
                return Promise.resolve(response);
              }
            });
            if (timeoutId) clearTimeout(timeoutId);
            removeScript(scriptId);
            clearFunction(callbackFunction);
          };
          url += url.indexOf("?") === -1 ? "?" : "&";
          var jsonpScript = document.createElement("script");
          jsonpScript.setAttribute("src", "" + url + jsonpCallback + "=" + callbackFunction);
          if (options.charset) {
            jsonpScript.setAttribute("charset", options.charset);
          }
          if (options.nonce) {
            jsonpScript.setAttribute("nonce", options.nonce);
          }
          if (options.referrerPolicy) {
            jsonpScript.setAttribute("referrerPolicy", options.referrerPolicy);
          }
          if (options.crossorigin) {
            jsonpScript.setAttribute("crossorigin", "true");
          }
          jsonpScript.id = scriptId;
          document.getElementsByTagName("head")[0].appendChild(jsonpScript);
          timeoutId = setTimeout(function() {
            reject(new Error("JSONP request to " + _url + " timed out"));
            clearFunction(callbackFunction);
            removeScript(scriptId);
            window[callbackFunction] = function() {
              clearFunction(callbackFunction);
            };
          }, timeout);
          jsonpScript.onerror = function() {
            reject(new Error("JSONP request to " + _url + " failed"));
            clearFunction(callbackFunction);
            removeScript(scriptId);
            if (timeoutId) clearTimeout(timeoutId);
          };
        });
      }
      module3.exports = fetchJsonp2;
    });
  })(fetchJsonp$1, fetchJsonp$1.exports);
  var fetchJsonpExports = fetchJsonp$1.exports;
  const fetchJsonp = /* @__PURE__ */ getDefaultExportFromCjs(fetchJsonpExports);
  function requestWithOpenserviceStr(serviceStr, params) {
    return new Promise((resolve, reject) => {
      if (!serviceStr) reject("no pagingUrl");
      let requestUrl = `//${transferDomain_1("open-s.alibaba.com")}/openservice/${serviceStr}`;
      let divideChar = "";
      if (requestUrl.indexOf("?") > -1) {
        divideChar = "&";
      } else {
        divideChar = "?";
      }
      if (params) {
        for (const [key, value] of Object.entries(params)) {
          requestUrl += `${divideChar}${key}=${encodeURIComponent(value)}`;
          divideChar = "&";
        }
      }
      fetchJsonp(requestUrl).then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error("network error");
        }
      }).then((res) => {
        if (res.code === 200) {
          resolve(res.data);
        } else {
          reject(res.msg);
        }
      }).catch((err) => {
        reject(err);
      });
    });
  }
  const SERVICE_MAP = {
    level1category: "categoryTabShowViewService",
    level1ToLeafCategory: "categoryShowOneToLeafViewService",
    level1ToLevel2Category: "categoryShowSecondViewService",
    level2ToLeafCategory: "categoryShowSecondToLeafViewService"
  };
  const getFirstCategoryList = () => {
    return requestWithOpenserviceStr(SERVICE_MAP.level1category);
  };
  const getLeafCategoryList = (categoryId) => {
    return requestWithOpenserviceStr(SERVICE_MAP.level1ToLeafCategory, {
      categoryId,
      showCategoryCount: "14"
    });
  };
  const getLevel2CategoryList = (level1CategoryId) => {
    return requestWithOpenserviceStr(SERVICE_MAP.level1ToLevel2Category, {
      categoryLevel: "1",
      categoryId: level1CategoryId
    });
  };
  const getLevel2ToLeafCategoryList = (level2CategoryId) => {
    return requestWithOpenserviceStr(SERVICE_MAP.level2ToLeafCategory, {
      categoryLevel: "2",
      categoryId: level2CategoryId
    });
  };
  const TreePanel = (props) => {
    const { categoryList = [], activeLevel1CategoryId, className, onClickHeader } = props;
    const category = categoryList.find((item) => item.categoryId === activeLevel1CategoryId);
    const [activeLevel2Category, setActiveLevel2Category] = React.useState({});
    const [leafList, setLeafList] = React.useState([]);
    const [level2CategoryList, setLevel2CategoryList] = React.useState([]);
    const cache = React.useRef({});
    const loadLeaves = (categoryId) => {
      if (!cache.current[categoryId]) {
        getLevel2ToLeafCategoryList(categoryId).then((data) => {
          const newLeaves = data.list || [];
          setLeafList(newLeaves);
          cache.current[categoryId] = newLeaves;
        });
      } else {
        setLeafList(cache.current[categoryId]);
      }
    };
    const handleLevel2Click = (item) => {
      setActiveLevel2Category(item);
      setLeafList([]);
    };
    React.useEffect(() => {
      getLevel2CategoryList(activeLevel1CategoryId).then((res) => {
        const newLeaves = res.list || [];
        getLevel2ToLeafCategoryList(newLeaves == null ? void 0 : newLeaves[0].categoryId).then((level2Data) => {
          const leafCategoryList = level2Data.list || [];
          setLevel2CategoryList(newLeaves);
          setLeafList(leafCategoryList);
          setActiveLevel2Category(newLeaves[0]);
        });
      });
    }, []);
    React.useEffect(() => {
      if (activeLevel2Category && activeLevel2Category.categoryId) {
        loadLeaves(activeLevel2Category.categoryId);
      }
    }, [activeLevel2Category]);
    return /* @__PURE__ */ React.createElement("div", { className: classnames("hc-tree-panel-container", className) }, /* @__PURE__ */ React.createElement("div", { className: "top-first-category-area", onClick: onClickHeader }, /* @__PURE__ */ React.createElement(
      "img",
      {
        className: "back-icon",
        src: LEFT_ARROW,
        "data-dot-header-categories": true,
        "data-params": `type=tree_panel_back&level1CategoryId=${activeLevel1CategoryId || ""}`
      }
    ), /* @__PURE__ */ React.createElement("div", { className: "title" }, category == null ? void 0 : category.title)), /* @__PURE__ */ React.createElement("div", { className: "content" }, /* @__PURE__ */ React.createElement("div", { className: "level2-list" }, level2CategoryList.length > 0 ? level2CategoryList.map((item) => {
      return /* @__PURE__ */ React.createElement(
        Level2Unit,
        __spreadProps(__spreadValues({
          key: `level2-unit-${item.categoryId}`
        }, item), {
          handleClick: () => handleLevel2Click(item),
          className: classnames({
            active: item.categoryId === activeLevel2Category.categoryId
          })
        })
      );
    }) : new Array(14).fill(null).map((_, index) => {
      return /* @__PURE__ */ React.createElement("div", { key: `placeholder-${index}`, className: "level2-placeholder" });
    })), /* @__PURE__ */ React.createElement("div", { className: "level3-list" }, activeLevel2Category && leafList.length > 0 ? /* @__PURE__ */ React.createElement("div", { className: "tree-panel-unit" }, /* @__PURE__ */ React.createElement("div", { className: "category-title" }, activeLevel2Category == null ? void 0 : activeLevel2Category.title), /* @__PURE__ */ React.createElement("div", { className: "leaf-container" }, leafList.map((leaf) => /* @__PURE__ */ React.createElement(
      Level3CategoryItem,
      {
        key: `leaf-${leaf.categoryId}`,
        icon: leaf == null ? void 0 : leaf.icon,
        imageUrl: leaf.imageUrl,
        action: leaf.action,
        dotParams: `level1CategoryId=${activeLevel1CategoryId || ""}&level2CategoryId=${activeLevel2Category.categoryId}&position=tree_panel`,
        categoryId: leaf.categoryId,
        title: leaf.title
      }
    )))) : /* @__PURE__ */ React.createElement("div", { className: "level3-placeholder-container" }, /* @__PURE__ */ React.createElement("div", { className: "title-placeholder" }), /* @__PURE__ */ React.createElement("div", { className: "list-placeholder" }, new Array(10).fill(null).map((_, index) => {
      return /* @__PURE__ */ React.createElement("div", { key: `placeholder-${index}`, className: "level3-placeholder-item" }, /* @__PURE__ */ React.createElement("div", { className: "placeholder-img" }), /* @__PURE__ */ React.createElement("div", { className: "placeholder-title" }));
    }))))));
  };
  const CategoryPanel = (props) => {
    const { className = "" } = props;
    const [categories, setCategories] = React.useState();
    const [viewAllText, setViewAllText] = React.useState();
    const [categoryEntryText, setCategoryEntryText] = React.useState();
    const [activeCategoryId, setActiveCategoryId] = React.useState(null);
    const [rightPanelIsScrolling, setRightPanelIsScrolling] = React.useState(false);
    const [treePanelVisible, setTreePanelVisible] = React.useState(false);
    const [isTreePanelEntering, setIsTreePanelEntering] = React.useState(false);
    const [rightPanelScrollType, setRightPanelScrollType] = React.useState("auto");
    const rightPanelRef = React.useRef(null);
    const modalRef = React.useRef(null);
    const cache = React.useRef({});
    const pendingRequests = React.useRef({});
    React.useEffect(() => {
      if (treePanelVisible) {
        requestAnimationFrame(() => {
          setIsTreePanelEntering(true);
        });
      } else {
        setIsTreePanelEntering(false);
      }
    }, [treePanelVisible]);
    const loadLeaves = (categoryId) => __async(this, null, function* () {
      if (cache.current[categoryId]) {
        return;
      }
      const existingRequest = pendingRequests.current[categoryId];
      if (existingRequest) {
        yield existingRequest;
        return;
      }
      const request = getLeafCategoryList(categoryId).then((data) => {
        const newLeaves = data.list;
        setCategories(
          (prevCategories) => prevCategories.map(
            (cat) => cat.categoryId === categoryId ? __spreadProps(__spreadValues({}, cat), { leaves: newLeaves }) : cat
          )
        );
        cache.current[categoryId] = newLeaves;
      }).finally(() => {
        delete pendingRequests.current[categoryId];
      });
      pendingRequests.current[categoryId] = request;
      yield request;
    });
    React.useEffect(() => {
      if (typeof window !== "undefined") {
        getFirstCategoryList().then((res) => {
          var _a, _b;
          setCategories(res == null ? void 0 : res.list);
          setViewAllText(res == null ? void 0 : res.viewAll);
          setCategoryEntryText(res == null ? void 0 : res.categoryEntryText);
          setActiveCategoryId((_b = (_a = res == null ? void 0 : res.list) == null ? void 0 : _a[0]) == null ? void 0 : _b.categoryId);
          const loadInitialCategories = () => __async(this, null, function* () {
            const promises = res.list.slice(0, 3).map((category) => loadLeaves(category == null ? void 0 : category.categoryId));
            yield Promise.all(promises);
          });
          loadInitialCategories();
        });
      }
      autoExp();
    }, []);
    React.useEffect(() => {
      if (!activeCategoryId || !categories.length) return;
      const categoryIndex = categories.findIndex((cat) => cat.categoryId === activeCategoryId);
      if (categoryIndex !== -1) {
        const preloadIds = [-2, -1, 0, 1, 2].map((offset) => {
          var _a;
          return (_a = categories[categoryIndex + offset]) == null ? void 0 : _a.categoryId;
        }).filter((id) => Boolean(id == null ? void 0 : id.trim()));
        Promise.all([...new Set(preloadIds)].map((id) => loadLeaves(id)));
      }
    }, [activeCategoryId]);
    React.useEffect(() => {
      if (!rightPanelRef.current || !activeCategoryId) return;
      let scrollTimeout;
      const handleScrollEnd = () => {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
          setRightPanelIsScrolling(false);
        }, 80);
      };
      const container = rightPanelRef.current;
      container.addEventListener("scroll", handleScrollEnd);
      return () => {
        if (container) {
          container.removeEventListener("scroll", handleScrollEnd);
        }
        clearTimeout(scrollTimeout);
      };
    }, [rightPanelRef, activeCategoryId]);
    const handleCategoryClick = (id) => {
      if (rightPanelIsScrolling) return;
      setActiveCategoryId(id);
      setRightPanelIsScrolling(true);
      setRightPanelScrollType("click");
      if (rightPanelRef.current) {
        const targetItem = rightPanelRef.current.querySelector(`[data-category-id="${id}"]`);
        if (targetItem) {
          const container = rightPanelRef.current;
          const containerRect = container.getBoundingClientRect();
          const targetRect = targetItem.getBoundingClientRect();
          const scrollTop = targetRect.top - containerRect.top + container.scrollTop;
          const startPosition = container.scrollTop;
          const distance = scrollTop - startPosition;
          const duration = 300;
          const startTime = performance.now();
          const animateScroll = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easing = progress < 0.5 ? 4 * progress * progress * progress : 1 - Math.pow(-2 * progress + 2, 3) / 2;
            container.scrollTop = startPosition + distance * easing;
            if (progress < 1) {
              requestAnimationFrame(animateScroll);
            } else {
              setRightPanelIsScrolling(false);
              setTimeout(() => {
                setRightPanelScrollType("auto");
              }, 500);
            }
          };
          requestAnimationFrame(animateScroll);
        }
      }
    };
    const scrollHandler = debounce(() => {
      if (!rightPanelRef.current || rightPanelScrollType === "click" || rightPanelIsScrolling) return;
      const items = rightPanelRef.current.querySelectorAll(".level3-panel-unit");
      const containerRect = rightPanelRef.current.getBoundingClientRect();
      const containerMidline = containerRect.top + containerRect.height / 2;
      let closestItem = null;
      let minDistance = Infinity;
      items.forEach((item) => {
        const itemRect = item.getBoundingClientRect();
        const itemCenter = itemRect.top + itemRect.height / 2;
        const distance = Math.abs(itemCenter - containerMidline);
        if (distance < minDistance) {
          minDistance = distance;
          closestItem = item;
        }
      });
      if (closestItem) {
        const { categoryId } = closestItem.dataset;
        if (!rightPanelIsScrolling && categoryId !== activeCategoryId) {
          setActiveCategoryId(categoryId);
          if (modalRef == null ? void 0 : modalRef.current) {
            const leftActiveItem = modalRef.current.querySelector(
              `[data-level1-category-id="${categoryId}"]`
            );
            if (leftActiveItem) {
              const container = modalRef.current.querySelector(".level1-panel-list");
              if (container) {
                const leftPanelRect = container.getBoundingClientRect();
                const targetRect = leftActiveItem.getBoundingClientRect();
                const isInViewport = targetRect.top >= leftPanelRect.top && targetRect.bottom <= leftPanelRect.bottom;
                if (!isInViewport) {
                  const containerCenter = leftPanelRect.top + leftPanelRect.height / 2;
                  const targetCenter = targetRect.top + targetRect.height / 2;
                  const scrollTop = container.scrollTop + (targetCenter - containerCenter);
                  const startPosition = container.scrollTop;
                  const distance = scrollTop - startPosition;
                  const duration = 300;
                  const startTime = performance.now();
                  const animateScroll = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    const easing = progress < 0.5 ? 4 * progress * progress * progress : 1 - Math.pow(-2 * progress + 2, 3) / 2;
                    container.scrollTop = startPosition + distance * easing;
                    if (progress < 1) {
                      requestAnimationFrame(animateScroll);
                    }
                  };
                  requestAnimationFrame(animateScroll);
                }
              }
            }
          }
        }
      }
    }, 300);
    const handleRightPanelScroll = (e) => {
      e.stopPropagation();
      scrollHandler();
    };
    const handleTreePanelClose = () => {
      manualClick({
        type: "tree_panel_back",
        level1CategoryId: activeCategoryId || ""
      });
      setIsTreePanelEntering(false);
      setTimeout(() => {
        setTreePanelVisible(false);
      }, 300);
    };
    return /* @__PURE__ */ React.createElement(
      "div",
      {
        className: classnames("header-category-panel", className),
        onWheel: (e) => e.stopPropagation()
      },
      /* @__PURE__ */ React.createElement(
        "div",
        {
          className: classnames("modal-panel-container", { "panel-fade": treePanelVisible }),
          ref: modalRef
        },
        /* @__PURE__ */ React.createElement(
          Level1Panel,
          {
            categoryList: categories,
            modalRef,
            rightPanelRef,
            activeCategoryId,
            onCategoryClick: handleCategoryClick,
            expanded: true
          }
        ),
        /* @__PURE__ */ React.createElement("div", { className: "hc-level3-panel" }, /* @__PURE__ */ React.createElement("div", { className: "hc-level3-list", ref: rightPanelRef, onScroll: handleRightPanelScroll }, categories == null ? void 0 : categories.map((category) => /* @__PURE__ */ React.createElement(
          Level3Unit,
          {
            key: `level3-unit-${category.categoryId}`,
            category,
            viewAllText,
            categoryEntryText,
            dotParams: `level1CategoryId=${category.categoryId}&position=modal_panel`,
            className: "level3-panel-unit",
            handleViewMoreClick: () => {
              setTreePanelVisible(true);
            },
            type: category.categoryId === "for_you" ? "prefer" : "leaf"
          }
        )))),
        treePanelVisible && activeCategoryId && /* @__PURE__ */ React.createElement(
          TreePanel,
          {
            activeLevel1CategoryId: activeCategoryId,
            categoryList: categories,
            onClickHeader: handleTreePanelClose,
            className: classnames({ "hc-panel-enter": isTreePanelEntering })
          }
        )
      )
    );
  };
  exports2.Fy24HeaderCategories = CategoryPanel;
  exports2.default = CategoryPanel;
  Object.defineProperties(exports2, { __esModule: { value: true }, [Symbol.toStringTag]: { value: "Module" } });
});
