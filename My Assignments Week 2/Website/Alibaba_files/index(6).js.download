(function(global2, factory) {
  typeof exports === "object" && typeof module !== "undefined" ? factory(exports, require("react")) : typeof define === "function" && define.amd ? define(["exports", "react"], factory) : (global2 = typeof globalThis !== "undefined" ? globalThis : global2 || self, factory(global2.HeaderShoppingCart = {}, global2.React));
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

  const i18n = {
    TitleWithAmount: "Shopping cart ({0} total)",
    AddCartSuccess: "Product added to cart!",
    TitleWithoutAmount: "Shopping cart",
    Empty: "Your cart is empty",
    GoToCart: "Go to cart",
    SkuInvalid: "Variation has expired",
    ProductInvalid: "Item has expired",
    NoSku: "No specification",
    SubtotalExclTax: "Subtotal excl. tax",
    Savings: "Savings: {0}"
  };
  let originGoldlog = { record: () => {
  } };
  if (typeof window !== "undefined") {
    originGoldlog = window.goldlog || {
      record: (logkey, gmkey, gokey) => {
        (window.goldlog_queue || (window.goldlog_queue = [])).push({
          action: "goldlog.record",
          arguments: [logkey, gmkey, gokey]
        });
      }
    };
  }
  const goldlog = (gokey, ext = null, type = "CLICK", logkey = "/sc.trade-cart.header-popup") => {
    if (!gokey || typeof window === "undefined") {
      return;
    }
    let strParams = `actionName=${gokey}`;
    if (ext instanceof Object) {
      try {
        let extParams = `actionName=${gokey}`;
        extParams = Object.keys(ext).map((key) => ext[key] instanceof Object ? `${key}=${JSON.stringify(ext[key])}` : `${key}=${ext[key]}`).join("&");
        strParams = `${strParams}&${extParams}`;
      } catch (err) {
      }
    }
    originGoldlog.record(logkey, type, strParams);
  };
  const reactTryCatchRender = ({ blockName = "", errorRenderComponent = null } = {}) => {
    return (ReactComponent) => {
      return class TryCatch extends React.Component {
        constructor() {
          super(...arguments);
          this.state = {
            hasError: false,
            error: null
          };
        }
        componentDidCatch(error) {
          this.setState({
            hasError: true,
            error
          });
          const { message } = error;
          const errorDetail = {
            isSuccess: false,
            actionType: "componentError",
            errorType: "componentError",
            actionName: message
          };
          goldlog(`render-error-${blockName}`, errorDetail);
        }
        render() {
          const { hasError, error } = this.state;
          if (!hasError) {
            return React.createElement(ReactComponent, this.props);
          }
          return errorRenderComponent && React.createElement(errorRenderComponent, { error });
        }
      };
    };
  };
  var commonjsGlobal = typeof globalThis !== "undefined" ? globalThis : typeof window !== "undefined" ? window : typeof global !== "undefined" ? global : typeof self !== "undefined" ? self : {};
  function getDefaultExportFromCjs(x) {
    return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, "default") ? x["default"] : x;
  }
  var fetchJsonp$1 = { exports: {} };
  (function(module2, exports$1) {
    (function(global2, factory) {
      {
        factory(exports$1, module2);
      }
    })(commonjsGlobal, function(exports$12, module3) {
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
  /*! js-cookie v3.0.5 | MIT */
  function assign(target) {
    for (var i = 1; i < arguments.length; i++) {
      var source = arguments[i];
      for (var key in source) {
        target[key] = source[key];
      }
    }
    return target;
  }
  var defaultConverter = {
    read: function(value) {
      if (value[0] === '"') {
        value = value.slice(1, -1);
      }
      return value.replace(/(%[\dA-F]{2})+/gi, decodeURIComponent);
    },
    write: function(value) {
      return encodeURIComponent(value).replace(
        /%(2[346BF]|3[AC-F]|40|5[BDE]|60|7[BCD])/g,
        decodeURIComponent
      );
    }
  };
  function init(converter, defaultAttributes) {
    function set(name, value, attributes) {
      if (typeof document === "undefined") {
        return;
      }
      attributes = assign({}, defaultAttributes, attributes);
      if (typeof attributes.expires === "number") {
        attributes.expires = new Date(Date.now() + attributes.expires * 864e5);
      }
      if (attributes.expires) {
        attributes.expires = attributes.expires.toUTCString();
      }
      name = encodeURIComponent(name).replace(/%(2[346B]|5E|60|7C)/g, decodeURIComponent).replace(/[()]/g, escape);
      var stringifiedAttributes = "";
      for (var attributeName in attributes) {
        if (!attributes[attributeName]) {
          continue;
        }
        stringifiedAttributes += "; " + attributeName;
        if (attributes[attributeName] === true) {
          continue;
        }
        stringifiedAttributes += "=" + attributes[attributeName].split(";")[0];
      }
      return document.cookie = name + "=" + converter.write(value, name) + stringifiedAttributes;
    }
    function get(name) {
      if (typeof document === "undefined" || arguments.length && !name) {
        return;
      }
      var cookies = document.cookie ? document.cookie.split("; ") : [];
      var jar = {};
      for (var i = 0; i < cookies.length; i++) {
        var parts = cookies[i].split("=");
        var value = parts.slice(1).join("=");
        try {
          var found = decodeURIComponent(parts[0]);
          jar[found] = converter.read(value, found);
          if (name === found) {
            break;
          }
        } catch (e) {
        }
      }
      return name ? jar[name] : jar;
    }
    return Object.create(
      {
        set,
        get,
        remove: function(name, attributes) {
          set(
            name,
            "",
            assign({}, attributes, {
              expires: -1
            })
          );
        },
        withAttributes: function(attributes) {
          return init(this.converter, assign({}, this.attributes, attributes));
        },
        withConverter: function(converter2) {
          return init(assign({}, this.converter, converter2), this.attributes);
        }
      },
      {
        attributes: { value: Object.freeze(defaultAttributes) },
        converter: { value: Object.freeze(converter) }
      }
    );
  }
  var api = init(defaultConverter, { path: "/" });
  const getSkuString = (skuNameValues) => {
    let skuString = "";
    try {
      if (skuNameValues && skuNameValues.length) {
        skuNameValues.forEach((item, index) => {
          if (index === skuNameValues.length - 1) {
            skuString += `${item.attrNameDesc}: ${item.attrValueDesc}`;
          } else {
            skuString += `${item.attrNameDesc}: ${item.attrValueDesc}; `;
          }
        });
      }
    } catch (error) {
      console.log(error);
    }
    return skuString;
  };
  const getNewSkuString = (skuNameValues) => {
    let skuString = "";
    try {
      if (skuNameValues && skuNameValues.length) {
        skuNameValues.forEach((item, index) => {
          if (index === skuNameValues.length - 1) {
            skuString += `${item.attrValueDesc}`;
          } else {
            skuString += `${item.attrValueDesc}, `;
          }
        });
      }
    } catch (error) {
      console.log(error);
    }
    return skuString;
  };
  const formatMoney = (money) => {
    const moneyStr = `${money}`;
    const moneyArr = moneyStr.split(".");
    const integerStr = moneyArr[0];
    const integerStrArr = integerStr.split("");
    const newIntegerStrArr = [];
    for (let start = 0; start < integerStrArr.length; start++) {
      if (start !== 0 && start % 3 === 0) {
        newIntegerStrArr.unshift(",");
      }
      newIntegerStrArr.unshift(integerStrArr[integerStrArr.length - 1 - start]);
    }
    moneyArr[0] = newIntegerStrArr.join("");
    return moneyArr.join(".");
  };
  const renderMoneyDtoAmountValue = (moneyDto) => {
    var _a, _b, _c;
    try {
      if ((_a = moneyDto == null ? void 0 : moneyDto.localizedMoney) == null ? void 0 : _a.localizedAmountString) {
        return moneyDto.localizedMoney.localizedAmountString;
      }
      if (((_b = moneyDto == null ? void 0 : moneyDto.money) == null ? void 0 : _b.amount) !== void 0 && ((_c = moneyDto == null ? void 0 : moneyDto.money) == null ? void 0 : _c.currency)) {
        return `${moneyDto.money.currency} ${formatMoney(moneyDto.money.amount.toFixed(2))}`;
      }
    } catch (error) {
      console.log("renderMoneyDtoAmountValue error:", error);
    }
    return "USD 0.00";
  };
  const getObjectCookieMap = (cookieName) => {
    const cfg = {};
    (api.get(cookieName) || "").split("&").forEach((str) => {
      const pair = str.split("=");
      if (pair[0]) {
        cfg[pair[0]] = pair[1];
      }
    });
    return cfg;
  };
  const getCtoken = () => {
    let json;
    try {
      const cookieName = "xman_us_t";
      json = getObjectCookieMap(cookieName);
    } catch (e) {
    }
    return (json == null ? void 0 : json.ctoken) || api.get("ctoken");
  };
  const getTbtoken = () => {
    let json;
    try {
      const cookieName = "sc_g_cfg_f";
      json = getObjectCookieMap(cookieName);
    } catch (e) {
    }
    return (json == null ? void 0 : json._tb_token_) || api.get("_tb_token_");
  };
  const getDomainSuffix = () => {
    const hostTemps = window.location.host.match(/(.*?).alibaba\.(.*?)$/);
    if (hostTemps && hostTemps.length >= 3) {
      return hostTemps[2];
    } else {
      return "com";
    }
  };
  const getCartData = () => __async(this, null, function* () {
    const url = `//carp.alibaba.${getDomainSuffix()}/simplePurchaseList.jsonp?_tb_token_=${getTbtoken()}&ctoken=${getCtoken()}`;
    return fetchJsonp(
      url,
      {
        timeout: 3e4
      }
    ).then((response) => response.json()).then((data) => {
      if (data.code === "200") {
        return data.response;
      } else {
        return {};
      }
    }).catch(() => {
      return {};
    });
  });
  function Skeleton(props) {
    return /* @__PURE__ */ React.createElement(
      "div",
      __spreadProps(__spreadValues({}, props), {
        className: (props == null ? void 0 : props.className) ? `header-cart-loading-container ${props.className}` : "header-cart-loading-container"
      }),
      /* @__PURE__ */ React.createElement("div", { className: "header-cart-block" }),
      /* @__PURE__ */ React.createElement("div", { className: "header-cart-block" }),
      /* @__PURE__ */ React.createElement("div", { className: "header-cart-block" })
    );
  }
  const emptyCart = () => {
    try {
      return /* @__PURE__ */ React.createElement("div", { className: "header-shopping-cart" }, /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-tltle" }, /* @__PURE__ */ React.createElement("span", null, i18n.TitleWithoutAmount)), /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-list" }, /* @__PURE__ */ React.createElement("div", { className: "empty-cart" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i2/O1CN01abjrJv1PIh1wh3e6j_!!6000000001818-2-tps-250-207.png", alt: "", dir: "ltr" }), /* @__PURE__ */ React.createElement("div", { className: "desc" }, i18n.Empty))), /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-actions shopping-cart-actions-empty" }, /* @__PURE__ */ React.createElement(
        "a",
        {
          className: "cart-action",
          href: "https://carp.alibaba.com/purchaseList",
          target: "_blank",
          rel: "noreferrer",
          onClick: () => {
            goldlog("go-to-cart");
          }
        },
        i18n.GoToCart
      )));
    } catch (error) {
      console.log(error);
    }
    return null;
  };
  const HeaderShoppingCart = reactTryCatchRender({
    blockName: "header-shopping-cart",
    errorRenderComponent: emptyCart
  })(({ cartNum, i18n: propsI18N, popupTiitle }) => {
    var _a;
    const i18n$1 = propsI18N ? __spreadValues(__spreadValues({}, i18n), propsI18N) : i18n;
    const [cartData, setCartData] = React.useState(window.cartDataCache || {});
    const [loading, setLoading] = React.useState(true);
    const { purchaseItemGroupList: supplierList = [], purchaseListStatisticsVO, purchaseCheckoutVO, abTestResultMap } = cartData || {};
    const { purchaseItemCount = cartNum } = purchaseListStatisticsVO || {};
    const initCartData = () => __async(this, null, function* () {
      if (window.cartDataCache) {
        setCartData(window.cartDataCache);
        setLoading(false);
      } else {
        const cartRes = yield getCartData();
        setCartData(cartRes);
        setLoading(false);
        window.cartDataCache = cartRes;
      }
    });
    React.useEffect(() => {
      initCartData();
      goldlog("enter-cart-popup", { purchaseItemCount });
    }, []);
    if (["exp1", "exp2"].includes((_a = abTestResultMap == null ? void 0 : abTestResultMap.carp_by_sku_pc) == null ? void 0 : _a.diversionResult)) {
      const { totalPrice, newTotalDiscountAmount } = purchaseCheckoutVO || {};
      return /* @__PURE__ */ React.createElement("div", { className: "header-shopping-cart header-shopping-cart-new-style" }, /* @__PURE__ */ React.createElement("div", { className: "header-shopping-content" }, /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-tltle" }, popupTiitle === "addCartSuccess" ? /* @__PURE__ */ React.createElement("span", { className: "success-tips" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i3/O1CN01J9Dv651bX8xGM2Rkf_!!6000000003474-2-tps-40-40.png", alt: "" }), /* @__PURE__ */ React.createElement("span", null, i18n$1.AddCartSuccess)) : /* @__PURE__ */ React.createElement("span", { dir: "auto" }, i18n$1.TitleWithoutAmount)), /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-list" }, loading ? /* @__PURE__ */ React.createElement("div", { className: "skeleton" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main-title" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-action" })), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" }))), purchaseItemCount && purchaseItemCount >= 2 ? /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main-title" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-action" })), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" }))) : null, purchaseItemCount && purchaseItemCount >= 3 ? /* @__PURE__ */ React.createElement("div", null, /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main-title" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-action" })), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" }))), /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main-title" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-action" })), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" })))) : null) : /* @__PURE__ */ React.createElement(React.Fragment, null, (supplierList == null ? void 0 : supplierList.length) ? supplierList.map((supplieItem) => {
        var _a2, _b, _c;
        const { purchaseItemBundleList: productList = [] } = supplieItem || {};
        return /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-list-item" }, /* @__PURE__ */ React.createElement(
          "a",
          {
            className: "company-name",
            dir: "ltr",
            href: (_a2 = supplieItem == null ? void 0 : supplieItem.companyInfo) == null ? void 0 : _a2.homepageUrl,
            title: (_b = supplieItem == null ? void 0 : supplieItem.companyInfo) == null ? void 0 : _b.companyName,
            target: "_blank",
            rel: "noreferrer",
            onClick: () => {
              goldlog("on-supplier-link-click");
            }
          },
          (_c = supplieItem == null ? void 0 : supplieItem.companyInfo) == null ? void 0 : _c.companyName
        ), (productList == null ? void 0 : productList.length) ? productList.map((productItem) => {
          const { tagInfoList = [], productImageUrl = "", productName, purchaseItemList: skuList = [], productDetailUrl, status: productStatus } = productItem || {};
          const semiManagedTag = (tagInfoList == null ? void 0 : tagInfoList.length) && tagInfoList.find((tagitem) => {
            return tagitem.position === "ABOVE" && tagitem.type === "SEMI_MANAGED";
          });
          const leftTagList = (tagInfoList == null ? void 0 : tagInfoList.length) && tagInfoList.filter((tagitem) => {
            return tagitem.position === "LEFT";
          });
          const productIsVaild = !(productStatus && productStatus === "invalid_out_of_date");
          return /* @__PURE__ */ React.createElement("div", { className: productIsVaild ? "product-item" : "product-item product-item-invalid" }, /* @__PURE__ */ React.createElement("div", { className: "product-content" }, semiManagedTag && semiManagedTag.tagImgUrl ? /* @__PURE__ */ React.createElement("img", { src: semiManagedTag.tagImgUrl, alt: "", className: "semi-managed-img" }) : null, /* @__PURE__ */ React.createElement(
            "a",
            {
              className: "product-name",
              href: productDetailUrl,
              title: productName,
              target: "_blank",
              rel: "noreferrer",
              onClick: () => {
                goldlog("on-product-item-click");
              }
            },
            Array.isArray(leftTagList) && leftTagList.length > 0 ? leftTagList.map((tagItem, idx) => {
              if (tagItem.tagImgUrl && tagItem.desc) {
                return /* @__PURE__ */ React.createElement(
                  "span",
                  {
                    className: "product-name-tag",
                    style: {
                      backgroundColor: tagItem.bgColor,
                      padding: "3px",
                      borderRadius: "2px",
                      marginInlineEnd: "4px",
                      height: "15px",
                      display: "inline-flex"
                    },
                    key: idx
                  },
                  /* @__PURE__ */ React.createElement("img", { src: tagItem.tagImgUrl, alt: "", style: { height: "9px", marginInlineEnd: "4px", display: "inline-block" } }),
                  /* @__PURE__ */ React.createElement("span", { style: { fontSize: "9px", lineHeight: "9px", fontWeight: "700", color: tagItem.textColor } }, tagItem.desc)
                );
              }
              return /* @__PURE__ */ React.createElement("span", { className: "product-name-tag", key: idx }, /* @__PURE__ */ React.createElement("img", { src: tagItem.tagImgUrl, alt: "", style: { height: "15px", marginInlineEnd: "4px", display: "inline-block" } }));
            }) : null,
            productName
          ), (skuList == null ? void 0 : skuList.length) && productIsVaild ? skuList.map((skuItem) => {
            var _a3, _b2, _c2, _d, _e;
            const { imageUrl = "", skuNameValues = [], quantity, unitPrice, originalUnitPrice, status: skuStatus, inventoryQuantity, customizationContent } = skuItem || {};
            let customizationString = "";
            if (customizationContent) {
              if (skuItem.customizationContent.details && ((_a3 = skuItem.customizationContent.details) == null ? void 0 : _a3.length)) {
                skuItem.customizationContent.details.forEach((contentDetail) => {
                  var _a4;
                  if (contentDetail.customizationPropertyList && ((_a4 = contentDetail.customizationPropertyList) == null ? void 0 : _a4.length)) {
                    contentDetail.customizationPropertyList.forEach((customizationProperty) => {
                      if (customizationString) {
                        customizationString = `${customizationString}, ${customizationProperty.value}`;
                      } else {
                        customizationString = customizationProperty.value;
                      }
                    });
                  }
                });
              }
            }
            const skuIsVaild = !(skuStatus === "invalid_out_of_date" || inventoryQuantity === 0);
            return /* @__PURE__ */ React.createElement("div", { className: "sku-item-container" }, /* @__PURE__ */ React.createElement("div", { className: "sku-img" }, /* @__PURE__ */ React.createElement("img", { src: imageUrl || productImageUrl, alt: "" })), /* @__PURE__ */ React.createElement("div", { className: skuIsVaild ? "sku-item" : "sku-item sku-item-invalid" }, /* @__PURE__ */ React.createElement("div", { className: "sku-content" }, /* @__PURE__ */ React.createElement("div", null, /* @__PURE__ */ React.createElement("div", { className: "sku-name" }, (skuNameValues == null ? void 0 : skuNameValues.length) ? /* @__PURE__ */ React.createElement("span", null, getNewSkuString(skuNameValues)) : /* @__PURE__ */ React.createElement("span", null, i18n$1.NoSku)), customizationString ? /* @__PURE__ */ React.createElement("div", { className: "sku-customization" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i4/O1CN01SEK1UZ1q4wozSlHzn_!!6000000005443-2-tps-32-32.png", alt: "" }), /* @__PURE__ */ React.createElement("span", null, customizationString)) : null), skuIsVaild ? /* @__PURE__ */ React.createElement("div", { className: "sku-price-amount" }, /* @__PURE__ */ React.createElement("div", { className: "sku-price", dir: "auto" }, /* @__PURE__ */ React.createElement("span", null, skuItem.unitPriceAfterPromotionMoneyDto ? renderMoneyDtoAmountValue(skuItem.unitPriceAfterPromotionMoneyDto) : renderMoneyDtoAmountValue(skuItem.unitPriceMoneyDto)), originalUnitPrice && (originalUnitPrice !== unitPrice || skuItem.unitPriceAfterPromotionMoneyDto && ((_c2 = (_b2 = skuItem.unitPriceAfterPromotionMoneyDto) == null ? void 0 : _b2.money) == null ? void 0 : _c2.amount) !== ((_e = (_d = skuItem.originalUnitPriceMoneyDto) == null ? void 0 : _d.money) == null ? void 0 : _e.amount)) ? /* @__PURE__ */ React.createElement("span", { className: "sku-original-price" }, renderMoneyDtoAmountValue(skuItem.originalUnitPriceMoneyDto)) : null), /* @__PURE__ */ React.createElement("div", { className: "sku-amount" }, /* @__PURE__ */ React.createElement(
              "span",
              {
                style: {
                  fontSize: "12px",
                  lineHeight: "16px",
                  marginTop: "2px",
                  display: "inline-block"
                }
              },
              "X"
            ), /* @__PURE__ */ React.createElement(
              "span",
              {
                style: { fontSize: "16px" },
                className: "sku-amount-quantity"
              },
              quantity
            ))) : /* @__PURE__ */ React.createElement("div", { className: "sku-item-invalid-desc" }, i18n$1.SkuInvalid))));
          }) : /* @__PURE__ */ React.createElement("div", { className: "product-item-invalid-desc" }, i18n$1.ProductInvalid)));
        }) : null);
      }) : /* @__PURE__ */ React.createElement("div", { className: "empty-cart" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i2/O1CN01abjrJv1PIh1wh3e6j_!!6000000001818-2-tps-250-207.png", alt: "", dir: "ltr" }), /* @__PURE__ */ React.createElement("div", { className: "desc" }, i18n$1.Empty)))), /* @__PURE__ */ React.createElement("div", { className: purchaseItemCount ? "shopping-cart-actions" : "shopping-cart-actions shopping-cart-actions-empty" }, loading ? /* @__PURE__ */ React.createElement(
        "div",
        {
          className: "cart-summary-item-container"
        },
        /* @__PURE__ */ React.createElement(
          "div",
          {
            className: "cart-summary-item"
          },
          /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-price-summary-left" }),
          /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-price-summary-right" })
        ),
        /* @__PURE__ */ React.createElement(
          "div",
          {
            className: "cart-summary-discount-item cart-summary-item"
          },
          /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-price-savings" })
        )
      ) : null, /* @__PURE__ */ React.createElement(
        "div",
        {
          className: "cart-summary-item-container"
        },
        totalPrice ? /* @__PURE__ */ React.createElement(
          "div",
          {
            className: "cart-summary-item"
          },
          /* @__PURE__ */ React.createElement("div", { className: "cart-summary-item-label" }, i18n$1.SubtotalExclTax),
          /* @__PURE__ */ React.createElement("div", { className: "cart-summary-item-value" }, renderMoneyDtoAmountValue(purchaseCheckoutVO == null ? void 0 : purchaseCheckoutVO.totalPriceMoneyDto))
        ) : null,
        newTotalDiscountAmount ? /* @__PURE__ */ React.createElement(
          "div",
          {
            className: "cart-summary-discount-item cart-summary-item"
          },
          /* @__PURE__ */ React.createElement("div", { className: "cart-summary-item-value" }, i18n$1.Savings.replace("{0}", renderMoneyDtoAmountValue(purchaseCheckoutVO == null ? void 0 : purchaseCheckoutVO.newTotalDiscountAmountMoneyDto)))
        ) : null
      ), /* @__PURE__ */ React.createElement(
        "a",
        {
          className: "cart-action",
          href: "https://carp.alibaba.com/purchaseList",
          target: "_blank",
          rel: "noreferrer",
          onClick: () => {
            goldlog("go-to-cart");
          }
        },
        i18n$1.GoToCart
      ))));
    }
    return /* @__PURE__ */ React.createElement("div", { className: "header-shopping-cart" }, /* @__PURE__ */ React.createElement("div", { className: "header-shopping-content" }, /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-tltle" }, popupTiitle === "addCartSuccess" ? /* @__PURE__ */ React.createElement("span", { className: "success-tips" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i3/O1CN01J9Dv651bX8xGM2Rkf_!!6000000003474-2-tps-40-40.png", alt: "" }), /* @__PURE__ */ React.createElement("span", null, i18n$1.AddCartSuccess)) : /* @__PURE__ */ React.createElement("span", null, i18n.TitleWithoutAmount)), /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-list" }, loading ? /* @__PURE__ */ React.createElement("div", { className: "skeleton" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-image" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-image" })), /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" }))), purchaseItemCount && purchaseItemCount >= 2 ? /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-image" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-image" })), /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" }))) : null, purchaseItemCount && purchaseItemCount >= 3 ? /* @__PURE__ */ React.createElement("div", null, /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-image" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-image" })), /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" }))), /* @__PURE__ */ React.createElement("div", { className: "skeleton-block" }, /* @__PURE__ */ React.createElement("div", { className: "skeleton-image" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-image" })), /* @__PURE__ */ React.createElement("div", { className: "skeleton-product-main" }, /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-title" }), /* @__PURE__ */ React.createElement(Skeleton, { className: "gray-sku" })))) : null) : /* @__PURE__ */ React.createElement(React.Fragment, null, (supplierList == null ? void 0 : supplierList.length) ? supplierList.map((supplieItem) => {
      var _a2, _b, _c;
      const { purchaseItemBundleList: productList = [] } = supplieItem || {};
      return /* @__PURE__ */ React.createElement("div", { className: "shopping-cart-list-item" }, /* @__PURE__ */ React.createElement(
        "a",
        {
          className: "company-name",
          dir: "ltr",
          href: (_a2 = supplieItem == null ? void 0 : supplieItem.companyInfo) == null ? void 0 : _a2.homepageUrl,
          title: (_b = supplieItem == null ? void 0 : supplieItem.companyInfo) == null ? void 0 : _b.companyName,
          target: "_blank",
          rel: "noreferrer",
          onClick: () => {
            goldlog("on-supplier-link-click");
          }
        },
        (_c = supplieItem == null ? void 0 : supplieItem.companyInfo) == null ? void 0 : _c.companyName
      ), (productList == null ? void 0 : productList.length) ? productList.map((productItem) => {
        const { tagInfoList = [], productImageUrl = "", productName, purchaseItemList: skuList = [], productDetailUrl, status: productStatus } = productItem || {};
        const semiManagedTag = (tagInfoList == null ? void 0 : tagInfoList.length) && tagInfoList.find((tagitem) => {
          return tagitem.position === "ABOVE" && tagitem.type === "SEMI_MANAGED";
        });
        const productIsVaild = !(productStatus && productStatus === "invalid_out_of_date");
        return /* @__PURE__ */ React.createElement("div", { className: productIsVaild ? "product-item" : "product-item product-item-invalid" }, /* @__PURE__ */ React.createElement(
          "a",
          {
            className: "product-img",
            href: productDetailUrl,
            target: "_blank",
            rel: "noreferrer",
            onClick: () => {
              goldlog("on-product-item-click");
            }
          },
          /* @__PURE__ */ React.createElement("img", { src: productImageUrl, alt: "" })
        ), /* @__PURE__ */ React.createElement("div", { className: "product-content" }, semiManagedTag && semiManagedTag.tagImgUrl ? /* @__PURE__ */ React.createElement("img", { src: semiManagedTag.tagImgUrl, alt: "", className: "semi-managed-img" }) : null, /* @__PURE__ */ React.createElement(
          "a",
          {
            className: "product-name",
            href: productDetailUrl,
            title: productName,
            target: "_blank",
            rel: "noreferrer",
            onClick: () => {
              goldlog("on-product-item-click");
            }
          },
          productName
        ), (skuList == null ? void 0 : skuList.length) && productIsVaild ? skuList.map((skuItem) => {
          var _a3;
          const { imageUrl = "", skuNameValues = [], quantity, status: skuStatus, inventoryQuantity, customizationContent } = skuItem || {};
          let customizationString = "";
          if (customizationContent) {
            if (skuItem.customizationContent.details && ((_a3 = skuItem.customizationContent.details) == null ? void 0 : _a3.length)) {
              skuItem.customizationContent.details.forEach((contentDetail) => {
                var _a4;
                if (contentDetail.customizationPropertyList && ((_a4 = contentDetail.customizationPropertyList) == null ? void 0 : _a4.length)) {
                  contentDetail.customizationPropertyList.forEach((customizationProperty) => {
                    if (customizationString) {
                      customizationString = `${customizationString}, ${customizationProperty.value}`;
                    } else {
                      customizationString = customizationProperty.value;
                    }
                  });
                }
              });
            }
          }
          const skuIsVaild = !(skuStatus === "invalid_out_of_date" || inventoryQuantity === 0);
          return /* @__PURE__ */ React.createElement("div", { className: skuIsVaild ? "sku-item" : "sku-item sku-item-invalid" }, /* @__PURE__ */ React.createElement("div", { className: "sku-img" }, /* @__PURE__ */ React.createElement("img", { src: imageUrl || productImageUrl, alt: "" })), /* @__PURE__ */ React.createElement("div", { className: "sku-content" }, /* @__PURE__ */ React.createElement("div", { className: "sku-name" }, (skuNameValues == null ? void 0 : skuNameValues.length) ? /* @__PURE__ */ React.createElement("span", null, getSkuString(skuNameValues)) : /* @__PURE__ */ React.createElement("span", null, i18n$1.NoSku)), customizationString ? /* @__PURE__ */ React.createElement("div", { className: "sku-customization" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i4/O1CN01SEK1UZ1q4wozSlHzn_!!6000000005443-2-tps-32-32.png", alt: "" }), /* @__PURE__ */ React.createElement("span", null, customizationString)) : null, skuIsVaild ? /* @__PURE__ */ React.createElement("div", { className: "sku-price-amount" }, /* @__PURE__ */ React.createElement("div", { className: "sku-price", dir: "auto" }, skuItem.unitPriceAfterPromotionMoneyDto ? renderMoneyDtoAmountValue(skuItem.unitPriceAfterPromotionMoneyDto) : renderMoneyDtoAmountValue(skuItem.unitPriceMoneyDto)), /* @__PURE__ */ React.createElement("div", { className: "sku-amount" }, /* @__PURE__ */ React.createElement("span", { style: { fontSize: "12px" } }, "X"), /* @__PURE__ */ React.createElement(
            "span",
            {
              style: { fontSize: "14px" },
              className: "sku-amount-quantity"
            },
            quantity
          ))) : /* @__PURE__ */ React.createElement("div", { className: "sku-item-invalid-desc" }, i18n$1.SkuInvalid)));
        }) : /* @__PURE__ */ React.createElement("div", { className: "product-item-invalid-desc" }, i18n$1.ProductInvalid)));
      }) : null);
    }) : /* @__PURE__ */ React.createElement("div", { className: "empty-cart" }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i2/O1CN01abjrJv1PIh1wh3e6j_!!6000000001818-2-tps-250-207.png", alt: "", dir: "ltr" }), /* @__PURE__ */ React.createElement("div", { className: "desc" }, i18n$1.Empty)))), /* @__PURE__ */ React.createElement("div", { className: purchaseItemCount ? "shopping-cart-actions" : "shopping-cart-actions shopping-cart-actions-empty" }, /* @__PURE__ */ React.createElement(
      "a",
      {
        className: "cart-action",
        href: "https://carp.alibaba.com/purchaseList",
        target: "_blank",
        rel: "noreferrer",
        onClick: () => {
          goldlog("go-to-cart");
        }
      },
      i18n$1.GoToCart
    ))));
  });
  exports2.HeaderShoppingCart = HeaderShoppingCart;
  exports2.default = HeaderShoppingCart;
  Object.defineProperties(exports2, { __esModule: { value: true }, [Symbol.toStringTag]: { value: "Module" } });
});
