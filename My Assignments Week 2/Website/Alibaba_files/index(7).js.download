(function(global2, factory) {
  typeof exports === "object" && typeof module !== "undefined" ? factory(exports, require("react"), require("react-dom")) : typeof define === "function" && define.amd ? define(["exports", "react", "react-dom"], factory) : (global2 = typeof globalThis !== "undefined" ? globalThis : global2 || self, factory(global2.ShipTo = {}, global2.React, global2.ReactDOM));
})(this, function(exports2, React, reactDom) {
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
var __objRest = (source, exclude) => {
  var target = {};
  for (var prop in source)
    if (__hasOwnProp.call(source, prop) && exclude.indexOf(prop) < 0)
      target[prop] = source[prop];
  if (source != null && __getOwnPropSymbols)
    for (var prop of __getOwnPropSymbols(source)) {
      if (exclude.indexOf(prop) < 0 && __propIsEnum.call(source, prop))
        target[prop] = source[prop];
    }
  return target;
};
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

  function _interopNamespaceDefault(e2) {
    const n2 = Object.create(null, { [Symbol.toStringTag]: { value: "Module" } });
    if (e2) {
      for (const k2 in e2) {
        if (k2 !== "default") {
          const d2 = Object.getOwnPropertyDescriptor(e2, k2);
          Object.defineProperty(n2, k2, d2.get ? d2 : {
            enumerable: true,
            get: () => e2[k2]
          });
        }
      }
    }
    n2.default = e2;
    return Object.freeze(n2);
  }
  const React__namespace = /* @__PURE__ */ _interopNamespaceDefault(React);
  /*! js-cookie v3.0.5 | MIT */
  function assign$1(target) {
    for (var i2 = 1; i2 < arguments.length; i2++) {
      var source = arguments[i2];
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
      attributes = assign$1({}, defaultAttributes, attributes);
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
      for (var i2 = 0; i2 < cookies.length; i2++) {
        var parts = cookies[i2].split("=");
        var value = parts.slice(1).join("=");
        try {
          var found = decodeURIComponent(parts[0]);
          jar[found] = converter.read(value, found);
          if (name === found) {
            break;
          }
        } catch (e2) {
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
            assign$1({}, attributes, {
              expires: -1
            })
          );
        },
        withAttributes: function(attributes) {
          return init(this.converter, assign$1({}, this.attributes, attributes));
        },
        withConverter: function(converter2) {
          return init(assign$1({}, this.converter, converter2), this.attributes);
        }
      },
      {
        attributes: { value: Object.freeze(defaultAttributes) },
        converter: { value: Object.freeze(converter) }
      }
    );
  }
  var api = init(defaultConverter, { path: "/" });
  const DEFAULT_COUNTRY = "US";
  const DEFAULT_CURRENCY = "USD";
  const DEFAULT_LANGUAGE = "en_US";
  const VALID_LIST_URL = "https://logistics.alibaba.com/luyou/shipto/list.htm?action=list";
  const VALID_ADD_URL = "https://logistics.alibaba.com/luyou/shipto/list.htm?action=add";
  const ZIP_CODE_REGEX = {
    AF: "^\\d{4}$",
    AX: "^22\\d{3}$",
    AL: "^\\d{4}$",
    DZ: "^\\d{5}$",
    AS: "^(96799)(?:[ \\-](\\d{4}))?$",
    AD: "^AD[1-7]0\\d$",
    AI: "^(?:AI-)?2640$",
    AR: "^((?:[A-HJ-NP-Z])?\\d{4})([A-Z]{3})?$",
    AM: "^(?:37)?\\d{4}$",
    AU: "^\\d{4}$",
    AT: "^\\d{4}$",
    AZ: "^\\d{4}$",
    BH: "^(?:\\d|1[0-2])\\d{2}$",
    BD: "^\\d{4}$",
    BB: "^BB\\d{5}$",
    BY: "^\\d{6}$",
    BE: "^\\d{4}$",
    BM: "^[A-Z]{2} ?[A-Z0-9]{2}$",
    BT: "^\\d{5}$",
    BA: "^\\d{5}$",
    BR: "^\\d{5}-?\\d{3}$",
    IO: "^BBND 1ZZ$",
    BN: "^[A-Z]{2} ?\\d{4}$",
    BG: "^\\d{4}$",
    KH: "^\\d{5}$",
    CA: "^[ABCEGHJKLMNPRSTVXY]\\d[ABCEGHJ-NPRSTV-Z] ?\\d[ABCEGHJ-NPRSTV-Z]\\d$",
    CV: "^\\d{4}$",
    KY: "^KY\\d-\\d{4}$",
    CL: "^\\d{7}$",
    CN: "^\\d{6}$",
    TW: "^\\d{3}(?:\\d{2})?$",
    CX: "^6798$",
    CC: "^6799$",
    CO: "^\\d{6}$",
    CR: "^\\d{4,5}|\\d{3}-\\d{4}$",
    HR: "^\\d{5}$",
    CY: "^\\d{4}$",
    CZ: "^\\d{3} ?\\d{2}$",
    DK: "^\\d{4}$",
    DO: "^\\d{5}$",
    EC: "^\\d{6}$",
    EG: "^\\d{5}$",
    SV: "^CP [1-3][1-7][0-2]\\d$",
    EE: "^\\d{5}$",
    ET: "^\\d{4}$",
    FK: "^FIQQ 1ZZ$",
    FO: "^\\d{3}$",
    FI: "^\\d{5}$",
    FR: "^\\d{2} ?\\d{3}$",
    GF: "^9[78]3\\d{2}$",
    PF: "^987\\d{2}$",
    GE: "^\\d{4}$",
    DE: "^\\d{5}$",
    GI: "^GX11 1AA$",
    GR: "^\\d{3} ?\\d{2}$",
    GL: "^39\\d{2}$",
    GP: "^9[78][01]\\d{2}$",
    GU: "^(969(?:[12]\\d|3[12]))(?:[ \\-](\\d{4}))?$",
    GT: "^\\d{5}$",
    GG: "^GY\\d[\\dA-Z]? ?\\d[ABD-HJLN-UW-Z]{2}$",
    GN: "^\\d{3}$",
    GW: "^\\d{4}$",
    HT: "^\\d{4}$",
    HM: "^\\d{4}$",
    HN: "^\\d{5}$",
    HU: "^\\d{4}$",
    IS: "^\\d{3}$",
    IN: "^\\d{6}$",
    ID: "^\\d{5}$",
    IR: "^\\d{5}-?\\d{5}$",
    IQ: "^\\d{5}$",
    IE: "^[\\dA-Z]{3} ?[\\dA-Z]{4}$",
    IM: "^IM\\d[\\dA-Z]? ?\\d[ABD-HJLN-UW-Z]{2}$",
    IL: "^\\d{5}(?:\\d{2})?$",
    IT: "^\\d{5}$",
    JP: "^\\d{3}-?\\d{4}$",
    JE: "^JE\\d[\\dA-Z]? ?\\d[ABD-HJLN-UW-Z]{2}$",
    JO: "^\\d{5}$",
    KZ: "^\\d{6}$",
    KE: "^\\d{5}$",
    KW: "^\\d{5}$",
    KG: "^\\d{6}$",
    LA: "^\\d{5}$",
    LV: "^LV-\\d{4}$",
    LB: "^(?:\\d{4})(?: ?(?:\\d{4}))?$",
    LS: "^\\d{3}$",
    LR: "^\\d{4}$",
    LI: "^948[5-9]|949[0-7]$",
    LT: "^\\d{5}$",
    LU: "^\\d{4}$",
    MK: "^\\d{4}$",
    MG: "^\\d{3}$",
    MY: "^\\d{5}$",
    MV: "^\\d{5}$",
    MT: "^[A-Z]{3} ?\\d{2,4}$",
    MH: "^(969[67]\\d)(?:[ \\-](\\d{4}))?$",
    MQ: "^9[78]2\\d{2}$",
    MU: "^\\d{3}(?:\\d{2}|[A-Z]{2}\\d{3})$",
    YT: "^976\\d{2}$",
    MX: "^\\d{5}$",
    FM: "^(9694[1-4])(?:[ \\-](\\d{4}))?$",
    MD: "^\\d{4}$",
    MC: "^980\\d{2}$",
    MN: "^\\d{5}$",
    ME: "^8\\d{4}$",
    MA: "^\\d{5}$",
    MZ: "^\\d{4}$",
    MM: "^\\d{5}$",
    NP: "^\\d{5}$",
    NL: "^\\d{4} ?[A-Z]{2}$",
    NC: "^988\\d{2}$",
    NZ: "^\\d{4}$",
    NI: "^\\d{5}$",
    NE: "^\\d{4}$",
    NG: "^\\d{6}$",
    NF: "^2899$",
    MP: "^(9695[012])(?:[ \\-](\\d{4}))?$",
    NO: "^\\d{4}$",
    OM: "^(?:PC )?\\d{3}$",
    PK: "^\\d{5}$",
    PW: "^(969(?:39|40))(?:[ \\-](\\d{4}))?$",
    PG: "^\\d{3}$",
    PY: "^\\d{4}$",
    PE: "^(?:LIMA \\d{1,2}|CALLAO 0?\\d)|[0-2]\\d{4}$",
    PH: "^\\d{4}$",
    PN: "^PCRN 1ZZ$",
    PL: "^\\d{2}-\\d{3}$",
    PT: "^\\d{4}-\\d{3}$",
    PR: "^(00[679]\\d{2})(?:[ \\-](\\d{4}))?$",
    RE: "^9[78]4\\d{2}$",
    RO: "^\\d{6}$",
    RU: "^\\d{6}$",
    BL: "^9[78][01]\\d{2}$",
    MF: "^9[78][01]\\d{2}$",
    VC: "^VC\\d{4}$",
    SM: "^4789\\d$",
    SA: "^\\d{5}$",
    SN: "^\\d{5}$",
    RS: "^\\d{5,6}$",
    SG: "^\\d{6}$",
    SK: "^\\d{3} ?\\d{2}$",
    SI: "^\\d{4}$",
    SO: "^[A-Z]{2} ?\\d{5}$",
    ZA: "^\\d{4}$",
    GS: "^SIQQ 1ZZ$",
    KR: "^\\d{5}$",
    ES: "^\\d{5}$",
    LK: "^\\d{5}$",
    SH: "^(?:ASCN|STHL) 1ZZ$",
    SJ: "^\\d{4}$",
    SZ: "^[HLMS]\\d{3}$",
    SE: "^\\d{3} ?\\d{2}$",
    CH: "^\\d{4}$",
    TJ: "^\\d{6}$",
    TZ: "^\\d{4,5}$",
    TH: "^\\d{5}$",
    TN: "^\\d{4}$",
    TR: "^\\d{5}$",
    TM: "^\\d{6}$",
    TC: "^TKCA 1ZZ$",
    UA: "^\\d{5}$",
    GB: "^GIR ?0AA|(?:(?:AB|AL|B|BA|BB|BD|BH|BL|BN|BR|BS|BT|BX|CA|CB|CF|CH|CM|CO|CR|CT|CV|CW|DA|DD|DE|DG|DH|DL|DN|DT|DY|E|EC|EH|EN|EX|FK|FY|G|GL|GY|GU|HA|HD|HG|HP|HR|HS|HU|HX|IG|IM|IP|IV|JE|KA|KT|KW|KY|L|LA|LD|LE|LL|LN|LS|LU|M|ME|MK|ML|N|NE|NG|NN|NP|NR|NW|OL|OX|PA|PE|PH|PL|PO|PR|RG|RH|RM|S|SA|SE|SG|SK|SL|SM|SN|SO|SP|SR|SS|ST|SW|SY|TA|TD|TF|TN|TQ|TR|TS|TW|UB|W|WA|WC|WD|WF|WN|WR|WS|WV|YO|ZE)(?:\\d[\\dA-Z]? ?\\d[ABD-HJLN-UW-Z]{2}))|BFPO ?\\d{1,4}$",
    US: "^(\\d{5})(?:[ \\-](\\d{4}))?$",
    UM: "^96898$",
    UY: "^\\d{5}$",
    UZ: "^\\d{6}$",
    VA: "^00120$",
    VE: "^\\d{4}$",
    VN: "^\\d{5,6}$",
    VG: "^VG\\d{4}$",
    VI: "^(008(?:(?:[0-4]\\d)|(?:5[01])))(?:[ \\-](\\d{4}))?$",
    WF: "^986\\d{2}$",
    EH: "^\\d{5}$",
    ZM: "^\\d{5}$"
  };
  const validateZipCode = (zipCodeValue, country) => {
    if (!zipCodeValue) return true;
    const regex = country && ZIP_CODE_REGEX[country] || "^(?=.*[a-zA-Z\\d])[a-zA-Z\\d\\s-]{1,16}$";
    return new RegExp(regex).test(`${zipCodeValue}`);
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
  const getLatestCookieData = function() {
    const cookieName = "sc_g_cfg_f";
    const cfg = getObjectCookieMap(cookieName);
    return {
      countryCode: cfg.sc_b_site,
      currencyCode: cfg.sc_b_currency || DEFAULT_CURRENCY,
      language: cfg.sc_b_locale || DEFAULT_LANGUAGE
    };
  };
  const getCtoken = () => {
    let json;
    try {
      const cookieName = "xman_us_t";
      json = getObjectCookieMap(cookieName);
    } catch (e2) {
    }
    return (json == null ? void 0 : json.ctoken) || api.get("ctoken");
  };
  const getIsLoggedIn = () => {
    const isLoginCookie = api.get("xman_us_t");
    return isLoginCookie && isLoginCookie.indexOf("sign=y") !== -1;
  };
  const Input$2 = ({
    value,
    country,
    onChange,
    className,
    isInvalid,
    setIsInvalid,
    i18n: i18n2
  }) => {
    React.useEffect(() => {
      if (!value) return setIsInvalid(false);
      handleValidateZipCode(value);
    }, [value, country]);
    const handleValidateZipCode = (zipCodeValue) => {
      const result = validateZipCode(zipCodeValue, country);
      setIsInvalid(!result);
      return result;
    };
    const handleOnChange = (e2) => {
      handleValidateZipCode(e2.target.value);
      onChange(e2);
    };
    return /* @__PURE__ */ React.createElement("div", { className }, /* @__PURE__ */ React.createElement(
      "input",
      {
        className: "input-zip-code",
        style: { borderColor: isInvalid ? "#B3261E" : "#c3c6cf" },
        value,
        onChange: handleOnChange,
        placeholder: i18n2[`sctnh.header_shipto_zipcode_placeholder_${country}`] || i18n2["sctnh.header_shipto_zipcode_placeholder"] || "Enter city or zip"
      }
    ), isInvalid && /* @__PURE__ */ React.createElement("span", { className: "input-invalid-text" }, i18n2[`sctnh.header_shipto_zipcode_invalid_${country}`] || i18n2["sctnh.header_shipto_zipcode_invalid"] || 'Invalid ZIP code. Example of the correct format: "1000".'));
  };
  const Loading = () => {
    return /* @__PURE__ */ React.createElement("div", { style: { fill: "#000", height: "20px", width: "20px", marginBottom: "12px" } }, /* @__PURE__ */ React.createElement("svg", { id: "loading", xmlns: "http://www.w3.org/2000/svg", viewBox: "0 0 32 32" }, /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(0 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(45 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.125s"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(90 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.25s"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(135 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.375s"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(180 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.5s"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(225 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.675s"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(270 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.75s"
      }
    )), /* @__PURE__ */ React.createElement("path", { opacity: ".1", d: "M14 0 H18 V8 H14 z", transform: "rotate(315 16 16)" }, /* @__PURE__ */ React.createElement(
      "animate",
      {
        attributeName: "opacity",
        from: "1",
        to: ".1",
        dur: "1s",
        repeatCount: "indefinite",
        begin: "0.875s"
      }
    ))));
  };
  function _typeof(o) {
    "@babel/helpers - typeof";
    return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(o2) {
      return typeof o2;
    } : function(o2) {
      return o2 && "function" == typeof Symbol && o2.constructor === Symbol && o2 !== Symbol.prototype ? "symbol" : typeof o2;
    }, _typeof(o);
  }
  function toPrimitive(t2, r2) {
    if ("object" != _typeof(t2) || !t2) return t2;
    var e2 = t2[Symbol.toPrimitive];
    if (void 0 !== e2) {
      var i2 = e2.call(t2, r2);
      if ("object" != _typeof(i2)) return i2;
      throw new TypeError("@@toPrimitive must return a primitive value.");
    }
    return ("string" === r2 ? String : Number)(t2);
  }
  function toPropertyKey(t2) {
    var i2 = toPrimitive(t2, "string");
    return "symbol" == _typeof(i2) ? i2 : i2 + "";
  }
  function _defineProperty(e2, r2, t2) {
    return (r2 = toPropertyKey(r2)) in e2 ? Object.defineProperty(e2, r2, {
      value: t2,
      enumerable: true,
      configurable: true,
      writable: true
    }) : e2[r2] = t2, e2;
  }
  function ownKeys(e2, r2) {
    var t2 = Object.keys(e2);
    if (Object.getOwnPropertySymbols) {
      var o = Object.getOwnPropertySymbols(e2);
      r2 && (o = o.filter(function(r3) {
        return Object.getOwnPropertyDescriptor(e2, r3).enumerable;
      })), t2.push.apply(t2, o);
    }
    return t2;
  }
  function _objectSpread2(e2) {
    for (var r2 = 1; r2 < arguments.length; r2++) {
      var t2 = null != arguments[r2] ? arguments[r2] : {};
      r2 % 2 ? ownKeys(Object(t2), true).forEach(function(r3) {
        _defineProperty(e2, r3, t2[r3]);
      }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e2, Object.getOwnPropertyDescriptors(t2)) : ownKeys(Object(t2)).forEach(function(r3) {
        Object.defineProperty(e2, r3, Object.getOwnPropertyDescriptor(t2, r3));
      });
    }
    return e2;
  }
  function _arrayWithHoles(r2) {
    if (Array.isArray(r2)) return r2;
  }
  function _iterableToArrayLimit(r2, l2) {
    var t2 = null == r2 ? null : "undefined" != typeof Symbol && r2[Symbol.iterator] || r2["@@iterator"];
    if (null != t2) {
      var e2, n2, i2, u, a = [], f2 = true, o = false;
      try {
        if (i2 = (t2 = t2.call(r2)).next, 0 === l2) {
          if (Object(t2) !== t2) return;
          f2 = false;
        } else for (; !(f2 = (e2 = i2.call(t2)).done) && (a.push(e2.value), a.length !== l2); f2 = true) ;
      } catch (r3) {
        o = true, n2 = r3;
      } finally {
        try {
          if (!f2 && null != t2["return"] && (u = t2["return"](), Object(u) !== u)) return;
        } finally {
          if (o) throw n2;
        }
      }
      return a;
    }
  }
  function _arrayLikeToArray(r2, a) {
    (null == a || a > r2.length) && (a = r2.length);
    for (var e2 = 0, n2 = Array(a); e2 < a; e2++) n2[e2] = r2[e2];
    return n2;
  }
  function _unsupportedIterableToArray(r2, a) {
    if (r2) {
      if ("string" == typeof r2) return _arrayLikeToArray(r2, a);
      var t2 = {}.toString.call(r2).slice(8, -1);
      return "Object" === t2 && r2.constructor && (t2 = r2.constructor.name), "Map" === t2 || "Set" === t2 ? Array.from(r2) : "Arguments" === t2 || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t2) ? _arrayLikeToArray(r2, a) : void 0;
    }
  }
  function _nonIterableRest() {
    throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
  }
  function _slicedToArray(r2, e2) {
    return _arrayWithHoles(r2) || _iterableToArrayLimit(r2, e2) || _unsupportedIterableToArray(r2, e2) || _nonIterableRest();
  }
  function _objectWithoutPropertiesLoose(r2, e2) {
    if (null == r2) return {};
    var t2 = {};
    for (var n2 in r2) if ({}.hasOwnProperty.call(r2, n2)) {
      if (-1 !== e2.indexOf(n2)) continue;
      t2[n2] = r2[n2];
    }
    return t2;
  }
  function _objectWithoutProperties(e2, t2) {
    if (null == e2) return {};
    var o, r2, i2 = _objectWithoutPropertiesLoose(e2, t2);
    if (Object.getOwnPropertySymbols) {
      var n2 = Object.getOwnPropertySymbols(e2);
      for (r2 = 0; r2 < n2.length; r2++) o = n2[r2], -1 === t2.indexOf(o) && {}.propertyIsEnumerable.call(e2, o) && (i2[o] = e2[o]);
    }
    return i2;
  }
  var _excluded$6 = ["defaultInputValue", "defaultMenuIsOpen", "defaultValue", "inputValue", "menuIsOpen", "onChange", "onInputChange", "onMenuClose", "onMenuOpen", "value"];
  function useStateManager(_ref3) {
    var _ref$defaultInputValu = _ref3.defaultInputValue, defaultInputValue = _ref$defaultInputValu === void 0 ? "" : _ref$defaultInputValu, _ref$defaultMenuIsOpe = _ref3.defaultMenuIsOpen, defaultMenuIsOpen = _ref$defaultMenuIsOpe === void 0 ? false : _ref$defaultMenuIsOpe, _ref$defaultValue = _ref3.defaultValue, defaultValue = _ref$defaultValue === void 0 ? null : _ref$defaultValue, propsInputValue = _ref3.inputValue, propsMenuIsOpen = _ref3.menuIsOpen, propsOnChange = _ref3.onChange, propsOnInputChange = _ref3.onInputChange, propsOnMenuClose = _ref3.onMenuClose, propsOnMenuOpen = _ref3.onMenuOpen, propsValue = _ref3.value, restSelectProps = _objectWithoutProperties(_ref3, _excluded$6);
    var _useState = React.useState(propsInputValue !== void 0 ? propsInputValue : defaultInputValue), _useState2 = _slicedToArray(_useState, 2), stateInputValue = _useState2[0], setStateInputValue = _useState2[1];
    var _useState3 = React.useState(propsMenuIsOpen !== void 0 ? propsMenuIsOpen : defaultMenuIsOpen), _useState4 = _slicedToArray(_useState3, 2), stateMenuIsOpen = _useState4[0], setStateMenuIsOpen = _useState4[1];
    var _useState5 = React.useState(propsValue !== void 0 ? propsValue : defaultValue), _useState6 = _slicedToArray(_useState5, 2), stateValue = _useState6[0], setStateValue = _useState6[1];
    var onChange = React.useCallback(function(value2, actionMeta) {
      if (typeof propsOnChange === "function") {
        propsOnChange(value2, actionMeta);
      }
      setStateValue(value2);
    }, [propsOnChange]);
    var onInputChange = React.useCallback(function(value2, actionMeta) {
      var newValue;
      if (typeof propsOnInputChange === "function") {
        newValue = propsOnInputChange(value2, actionMeta);
      }
      setStateInputValue(newValue !== void 0 ? newValue : value2);
    }, [propsOnInputChange]);
    var onMenuOpen = React.useCallback(function() {
      if (typeof propsOnMenuOpen === "function") {
        propsOnMenuOpen();
      }
      setStateMenuIsOpen(true);
    }, [propsOnMenuOpen]);
    var onMenuClose = React.useCallback(function() {
      if (typeof propsOnMenuClose === "function") {
        propsOnMenuClose();
      }
      setStateMenuIsOpen(false);
    }, [propsOnMenuClose]);
    var inputValue = propsInputValue !== void 0 ? propsInputValue : stateInputValue;
    var menuIsOpen = propsMenuIsOpen !== void 0 ? propsMenuIsOpen : stateMenuIsOpen;
    var value = propsValue !== void 0 ? propsValue : stateValue;
    return _objectSpread2(_objectSpread2({}, restSelectProps), {}, {
      inputValue,
      menuIsOpen,
      onChange,
      onInputChange,
      onMenuClose,
      onMenuOpen,
      value
    });
  }
  function _extends() {
    return _extends = Object.assign ? Object.assign.bind() : function(n2) {
      for (var e2 = 1; e2 < arguments.length; e2++) {
        var t2 = arguments[e2];
        for (var r2 in t2) ({}).hasOwnProperty.call(t2, r2) && (n2[r2] = t2[r2]);
      }
      return n2;
    }, _extends.apply(null, arguments);
  }
  function _classCallCheck(a, n2) {
    if (!(a instanceof n2)) throw new TypeError("Cannot call a class as a function");
  }
  function _defineProperties(e2, r2) {
    for (var t2 = 0; t2 < r2.length; t2++) {
      var o = r2[t2];
      o.enumerable = o.enumerable || false, o.configurable = true, "value" in o && (o.writable = true), Object.defineProperty(e2, toPropertyKey(o.key), o);
    }
  }
  function _createClass(e2, r2, t2) {
    return r2 && _defineProperties(e2.prototype, r2), t2 && _defineProperties(e2, t2), Object.defineProperty(e2, "prototype", {
      writable: false
    }), e2;
  }
  function _setPrototypeOf(t2, e2) {
    return _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(t3, e3) {
      return t3.__proto__ = e3, t3;
    }, _setPrototypeOf(t2, e2);
  }
  function _inherits(t2, e2) {
    if ("function" != typeof e2 && null !== e2) throw new TypeError("Super expression must either be null or a function");
    t2.prototype = Object.create(e2 && e2.prototype, {
      constructor: {
        value: t2,
        writable: true,
        configurable: true
      }
    }), Object.defineProperty(t2, "prototype", {
      writable: false
    }), e2 && _setPrototypeOf(t2, e2);
  }
  function _getPrototypeOf(t2) {
    return _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t3) {
      return t3.__proto__ || Object.getPrototypeOf(t3);
    }, _getPrototypeOf(t2);
  }
  function _isNativeReflectConstruct() {
    try {
      var t2 = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
      }));
    } catch (t3) {
    }
    return (_isNativeReflectConstruct = function _isNativeReflectConstruct2() {
      return !!t2;
    })();
  }
  function _assertThisInitialized(e2) {
    if (void 0 === e2) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
    return e2;
  }
  function _possibleConstructorReturn(t2, e2) {
    if (e2 && ("object" == _typeof(e2) || "function" == typeof e2)) return e2;
    if (void 0 !== e2) throw new TypeError("Derived constructors may only return object or undefined");
    return _assertThisInitialized(t2);
  }
  function _createSuper(t2) {
    var r2 = _isNativeReflectConstruct();
    return function() {
      var e2, o = _getPrototypeOf(t2);
      if (r2) {
        var s = _getPrototypeOf(this).constructor;
        e2 = Reflect.construct(o, arguments, s);
      } else e2 = o.apply(this, arguments);
      return _possibleConstructorReturn(this, e2);
    };
  }
  function _arrayWithoutHoles(r2) {
    if (Array.isArray(r2)) return _arrayLikeToArray(r2);
  }
  function _iterableToArray(r2) {
    if ("undefined" != typeof Symbol && null != r2[Symbol.iterator] || null != r2["@@iterator"]) return Array.from(r2);
  }
  function _nonIterableSpread() {
    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
  }
  function _toConsumableArray(r2) {
    return _arrayWithoutHoles(r2) || _iterableToArray(r2) || _unsupportedIterableToArray(r2) || _nonIterableSpread();
  }
  function sheetForTag(tag) {
    if (tag.sheet) {
      return tag.sheet;
    }
    for (var i2 = 0; i2 < document.styleSheets.length; i2++) {
      if (document.styleSheets[i2].ownerNode === tag) {
        return document.styleSheets[i2];
      }
    }
    return void 0;
  }
  function createStyleElement(options2) {
    var tag = document.createElement("style");
    tag.setAttribute("data-emotion", options2.key);
    if (options2.nonce !== void 0) {
      tag.setAttribute("nonce", options2.nonce);
    }
    tag.appendChild(document.createTextNode(""));
    tag.setAttribute("data-s", "");
    return tag;
  }
  var StyleSheet = /* @__PURE__ */ function() {
    function StyleSheet2(options2) {
      var _this = this;
      this._insertTag = function(tag) {
        var before;
        if (_this.tags.length === 0) {
          if (_this.insertionPoint) {
            before = _this.insertionPoint.nextSibling;
          } else if (_this.prepend) {
            before = _this.container.firstChild;
          } else {
            before = _this.before;
          }
        } else {
          before = _this.tags[_this.tags.length - 1].nextSibling;
        }
        _this.container.insertBefore(tag, before);
        _this.tags.push(tag);
      };
      this.isSpeedy = options2.speedy === void 0 ? true : options2.speedy;
      this.tags = [];
      this.ctr = 0;
      this.nonce = options2.nonce;
      this.key = options2.key;
      this.container = options2.container;
      this.prepend = options2.prepend;
      this.insertionPoint = options2.insertionPoint;
      this.before = null;
    }
    var _proto = StyleSheet2.prototype;
    _proto.hydrate = function hydrate(nodes) {
      nodes.forEach(this._insertTag);
    };
    _proto.insert = function insert(rule) {
      if (this.ctr % (this.isSpeedy ? 65e3 : 1) === 0) {
        this._insertTag(createStyleElement(this));
      }
      var tag = this.tags[this.tags.length - 1];
      if (this.isSpeedy) {
        var sheet = sheetForTag(tag);
        try {
          sheet.insertRule(rule, sheet.cssRules.length);
        } catch (e2) {
        }
      } else {
        tag.appendChild(document.createTextNode(rule));
      }
      this.ctr++;
    };
    _proto.flush = function flush() {
      this.tags.forEach(function(tag) {
        var _tag$parentNode;
        return (_tag$parentNode = tag.parentNode) == null ? void 0 : _tag$parentNode.removeChild(tag);
      });
      this.tags = [];
      this.ctr = 0;
    };
    return StyleSheet2;
  }();
  var MS = "-ms-";
  var MOZ = "-moz-";
  var WEBKIT = "-webkit-";
  var COMMENT = "comm";
  var RULESET = "rule";
  var DECLARATION = "decl";
  var IMPORT = "@import";
  var KEYFRAMES = "@keyframes";
  var LAYER = "@layer";
  var abs = Math.abs;
  var from = String.fromCharCode;
  var assign = Object.assign;
  function hash(value, length2) {
    return charat(value, 0) ^ 45 ? (((length2 << 2 ^ charat(value, 0)) << 2 ^ charat(value, 1)) << 2 ^ charat(value, 2)) << 2 ^ charat(value, 3) : 0;
  }
  function trim(value) {
    return value.trim();
  }
  function match(value, pattern) {
    return (value = pattern.exec(value)) ? value[0] : value;
  }
  function replace(value, pattern, replacement) {
    return value.replace(pattern, replacement);
  }
  function indexof(value, search) {
    return value.indexOf(search);
  }
  function charat(value, index2) {
    return value.charCodeAt(index2) | 0;
  }
  function substr(value, begin, end) {
    return value.slice(begin, end);
  }
  function strlen(value) {
    return value.length;
  }
  function sizeof(value) {
    return value.length;
  }
  function append(value, array) {
    return array.push(value), value;
  }
  function combine(array, callback) {
    return array.map(callback).join("");
  }
  var line = 1;
  var column = 1;
  var length = 0;
  var position = 0;
  var character = 0;
  var characters = "";
  function node(value, root, parent, type, props, children, length2) {
    return { value, root, parent, type, props, children, line, column, length: length2, return: "" };
  }
  function copy(root, props) {
    return assign(node("", null, null, "", null, null, 0), root, { length: -root.length }, props);
  }
  function char() {
    return character;
  }
  function prev() {
    character = position > 0 ? charat(characters, --position) : 0;
    if (column--, character === 10)
      column = 1, line--;
    return character;
  }
  function next() {
    character = position < length ? charat(characters, position++) : 0;
    if (column++, character === 10)
      column = 1, line++;
    return character;
  }
  function peek() {
    return charat(characters, position);
  }
  function caret() {
    return position;
  }
  function slice(begin, end) {
    return substr(characters, begin, end);
  }
  function token(type) {
    switch (type) {
      case 0:
      case 9:
      case 10:
      case 13:
      case 32:
        return 5;
      case 33:
      case 43:
      case 44:
      case 47:
      case 62:
      case 64:
      case 126:
      case 59:
      case 123:
      case 125:
        return 4;
      case 58:
        return 3;
      case 34:
      case 39:
      case 40:
      case 91:
        return 2;
      case 41:
      case 93:
        return 1;
    }
    return 0;
  }
  function alloc(value) {
    return line = column = 1, length = strlen(characters = value), position = 0, [];
  }
  function dealloc(value) {
    return characters = "", value;
  }
  function delimit(type) {
    return trim(slice(position - 1, delimiter(type === 91 ? type + 2 : type === 40 ? type + 1 : type)));
  }
  function whitespace(type) {
    while (character = peek())
      if (character < 33)
        next();
      else
        break;
    return token(type) > 2 || token(character) > 3 ? "" : " ";
  }
  function escaping(index2, count) {
    while (--count && next())
      if (character < 48 || character > 102 || character > 57 && character < 65 || character > 70 && character < 97)
        break;
    return slice(index2, caret() + (count < 6 && peek() == 32 && next() == 32));
  }
  function delimiter(type) {
    while (next())
      switch (character) {
        case type:
          return position;
        case 34:
        case 39:
          if (type !== 34 && type !== 39)
            delimiter(character);
          break;
        case 40:
          if (type === 41)
            delimiter(type);
          break;
        case 92:
          next();
          break;
      }
    return position;
  }
  function commenter(type, index2) {
    while (next())
      if (type + character === 47 + 10)
        break;
      else if (type + character === 42 + 42 && peek() === 47)
        break;
    return "/*" + slice(index2, position - 1) + "*" + from(type === 47 ? type : next());
  }
  function identifier(index2) {
    while (!token(peek()))
      next();
    return slice(index2, position);
  }
  function compile(value) {
    return dealloc(parse("", null, null, null, [""], value = alloc(value), 0, [0], value));
  }
  function parse(value, root, parent, rule, rules, rulesets, pseudo, points, declarations) {
    var index2 = 0;
    var offset = 0;
    var length2 = pseudo;
    var atrule = 0;
    var property = 0;
    var previous = 0;
    var variable = 1;
    var scanning = 1;
    var ampersand = 1;
    var character2 = 0;
    var type = "";
    var props = rules;
    var children = rulesets;
    var reference = rule;
    var characters2 = type;
    while (scanning)
      switch (previous = character2, character2 = next()) {
        case 40:
          if (previous != 108 && charat(characters2, length2 - 1) == 58) {
            if (indexof(characters2 += replace(delimit(character2), "&", "&\f"), "&\f") != -1)
              ampersand = -1;
            break;
          }
        case 34:
        case 39:
        case 91:
          characters2 += delimit(character2);
          break;
        case 9:
        case 10:
        case 13:
        case 32:
          characters2 += whitespace(previous);
          break;
        case 92:
          characters2 += escaping(caret() - 1, 7);
          continue;
        case 47:
          switch (peek()) {
            case 42:
            case 47:
              append(comment(commenter(next(), caret()), root, parent), declarations);
              break;
            default:
              characters2 += "/";
          }
          break;
        case 123 * variable:
          points[index2++] = strlen(characters2) * ampersand;
        case 125 * variable:
        case 59:
        case 0:
          switch (character2) {
            case 0:
            case 125:
              scanning = 0;
            case 59 + offset:
              if (ampersand == -1) characters2 = replace(characters2, /\f/g, "");
              if (property > 0 && strlen(characters2) - length2)
                append(property > 32 ? declaration(characters2 + ";", rule, parent, length2 - 1) : declaration(replace(characters2, " ", "") + ";", rule, parent, length2 - 2), declarations);
              break;
            case 59:
              characters2 += ";";
            default:
              append(reference = ruleset(characters2, root, parent, index2, offset, rules, points, type, props = [], children = [], length2), rulesets);
              if (character2 === 123)
                if (offset === 0)
                  parse(characters2, root, reference, reference, props, rulesets, length2, points, children);
                else
                  switch (atrule === 99 && charat(characters2, 3) === 110 ? 100 : atrule) {
                    case 100:
                    case 108:
                    case 109:
                    case 115:
                      parse(value, reference, reference, rule && append(ruleset(value, reference, reference, 0, 0, rules, points, type, rules, props = [], length2), children), rules, children, length2, points, rule ? props : children);
                      break;
                    default:
                      parse(characters2, reference, reference, reference, [""], children, 0, points, children);
                  }
          }
          index2 = offset = property = 0, variable = ampersand = 1, type = characters2 = "", length2 = pseudo;
          break;
        case 58:
          length2 = 1 + strlen(characters2), property = previous;
        default:
          if (variable < 1) {
            if (character2 == 123)
              --variable;
            else if (character2 == 125 && variable++ == 0 && prev() == 125)
              continue;
          }
          switch (characters2 += from(character2), character2 * variable) {
            case 38:
              ampersand = offset > 0 ? 1 : (characters2 += "\f", -1);
              break;
            case 44:
              points[index2++] = (strlen(characters2) - 1) * ampersand, ampersand = 1;
              break;
            case 64:
              if (peek() === 45)
                characters2 += delimit(next());
              atrule = peek(), offset = length2 = strlen(type = characters2 += identifier(caret())), character2++;
              break;
            case 45:
              if (previous === 45 && strlen(characters2) == 2)
                variable = 0;
          }
      }
    return rulesets;
  }
  function ruleset(value, root, parent, index2, offset, rules, points, type, props, children, length2) {
    var post = offset - 1;
    var rule = offset === 0 ? rules : [""];
    var size = sizeof(rule);
    for (var i2 = 0, j2 = 0, k2 = 0; i2 < index2; ++i2)
      for (var x2 = 0, y2 = substr(value, post + 1, post = abs(j2 = points[i2])), z2 = value; x2 < size; ++x2)
        if (z2 = trim(j2 > 0 ? rule[x2] + " " + y2 : replace(y2, /&\f/g, rule[x2])))
          props[k2++] = z2;
    return node(value, root, parent, offset === 0 ? RULESET : type, props, children, length2);
  }
  function comment(value, root, parent) {
    return node(value, root, parent, COMMENT, from(char()), substr(value, 2, -2), 0);
  }
  function declaration(value, root, parent, length2) {
    return node(value, root, parent, DECLARATION, substr(value, 0, length2), substr(value, length2 + 1, -1), length2);
  }
  function serialize(children, callback) {
    var output = "";
    var length2 = sizeof(children);
    for (var i2 = 0; i2 < length2; i2++)
      output += callback(children[i2], i2, children, callback) || "";
    return output;
  }
  function stringify(element, index2, children, callback) {
    switch (element.type) {
      case LAYER:
        if (element.children.length) break;
      case IMPORT:
      case DECLARATION:
        return element.return = element.return || element.value;
      case COMMENT:
        return "";
      case KEYFRAMES:
        return element.return = element.value + "{" + serialize(element.children, callback) + "}";
      case RULESET:
        element.value = element.props.join(",");
    }
    return strlen(children = serialize(element.children, callback)) ? element.return = element.value + "{" + children + "}" : "";
  }
  function middleware(collection) {
    var length2 = sizeof(collection);
    return function(element, index2, children, callback) {
      var output = "";
      for (var i2 = 0; i2 < length2; i2++)
        output += collection[i2](element, index2, children, callback) || "";
      return output;
    };
  }
  function rulesheet(callback) {
    return function(element) {
      if (!element.root) {
        if (element = element.return)
          callback(element);
      }
    };
  }
  function memoize(fn) {
    var cache = /* @__PURE__ */ Object.create(null);
    return function(arg) {
      if (cache[arg] === void 0) cache[arg] = fn(arg);
      return cache[arg];
    };
  }
  var identifierWithPointTracking = function identifierWithPointTracking2(begin, points, index2) {
    var previous = 0;
    var character2 = 0;
    while (true) {
      previous = character2;
      character2 = peek();
      if (previous === 38 && character2 === 12) {
        points[index2] = 1;
      }
      if (token(character2)) {
        break;
      }
      next();
    }
    return slice(begin, position);
  };
  var toRules = function toRules2(parsed, points) {
    var index2 = -1;
    var character2 = 44;
    do {
      switch (token(character2)) {
        case 0:
          if (character2 === 38 && peek() === 12) {
            points[index2] = 1;
          }
          parsed[index2] += identifierWithPointTracking(position - 1, points, index2);
          break;
        case 2:
          parsed[index2] += delimit(character2);
          break;
        case 4:
          if (character2 === 44) {
            parsed[++index2] = peek() === 58 ? "&\f" : "";
            points[index2] = parsed[index2].length;
            break;
          }
        default:
          parsed[index2] += from(character2);
      }
    } while (character2 = next());
    return parsed;
  };
  var getRules = function getRules2(value, points) {
    return dealloc(toRules(alloc(value), points));
  };
  var fixedElements = /* @__PURE__ */ new WeakMap();
  var compat = function compat2(element) {
    if (element.type !== "rule" || !element.parent || // positive .length indicates that this rule contains pseudo
    // negative .length indicates that this rule has been already prefixed
    element.length < 1) {
      return;
    }
    var value = element.value;
    var parent = element.parent;
    var isImplicitRule = element.column === parent.column && element.line === parent.line;
    while (parent.type !== "rule") {
      parent = parent.parent;
      if (!parent) return;
    }
    if (element.props.length === 1 && value.charCodeAt(0) !== 58 && !fixedElements.get(parent)) {
      return;
    }
    if (isImplicitRule) {
      return;
    }
    fixedElements.set(element, true);
    var points = [];
    var rules = getRules(value, points);
    var parentRules = parent.props;
    for (var i2 = 0, k2 = 0; i2 < rules.length; i2++) {
      for (var j2 = 0; j2 < parentRules.length; j2++, k2++) {
        element.props[k2] = points[i2] ? rules[i2].replace(/&\f/g, parentRules[j2]) : parentRules[j2] + " " + rules[i2];
      }
    }
  };
  var removeLabel = function removeLabel2(element) {
    if (element.type === "decl") {
      var value = element.value;
      if (
        // charcode for l
        value.charCodeAt(0) === 108 && // charcode for b
        value.charCodeAt(2) === 98
      ) {
        element["return"] = "";
        element.value = "";
      }
    }
  };
  function prefix(value, length2) {
    switch (hash(value, length2)) {
      case 5103:
        return WEBKIT + "print-" + value + value;
      case 5737:
      case 4201:
      case 3177:
      case 3433:
      case 1641:
      case 4457:
      case 2921:
      case 5572:
      case 6356:
      case 5844:
      case 3191:
      case 6645:
      case 3005:
      case 6391:
      case 5879:
      case 5623:
      case 6135:
      case 4599:
      case 4855:
      case 4215:
      case 6389:
      case 5109:
      case 5365:
      case 5621:
      case 3829:
        return WEBKIT + value + value;
      case 5349:
      case 4246:
      case 4810:
      case 6968:
      case 2756:
        return WEBKIT + value + MOZ + value + MS + value + value;
      case 6828:
      case 4268:
        return WEBKIT + value + MS + value + value;
      case 6165:
        return WEBKIT + value + MS + "flex-" + value + value;
      case 5187:
        return WEBKIT + value + replace(value, /(\w+).+(:[^]+)/, WEBKIT + "box-$1$2" + MS + "flex-$1$2") + value;
      case 5443:
        return WEBKIT + value + MS + "flex-item-" + replace(value, /flex-|-self/, "") + value;
      case 4675:
        return WEBKIT + value + MS + "flex-line-pack" + replace(value, /align-content|flex-|-self/, "") + value;
      case 5548:
        return WEBKIT + value + MS + replace(value, "shrink", "negative") + value;
      case 5292:
        return WEBKIT + value + MS + replace(value, "basis", "preferred-size") + value;
      case 6060:
        return WEBKIT + "box-" + replace(value, "-grow", "") + WEBKIT + value + MS + replace(value, "grow", "positive") + value;
      case 4554:
        return WEBKIT + replace(value, /([^-])(transform)/g, "$1" + WEBKIT + "$2") + value;
      case 6187:
        return replace(replace(replace(value, /(zoom-|grab)/, WEBKIT + "$1"), /(image-set)/, WEBKIT + "$1"), value, "") + value;
      case 5495:
      case 3959:
        return replace(value, /(image-set\([^]*)/, WEBKIT + "$1$`$1");
      case 4968:
        return replace(replace(value, /(.+:)(flex-)?(.*)/, WEBKIT + "box-pack:$3" + MS + "flex-pack:$3"), /s.+-b[^;]+/, "justify") + WEBKIT + value + value;
      case 4095:
      case 3583:
      case 4068:
      case 2532:
        return replace(value, /(.+)-inline(.+)/, WEBKIT + "$1$2") + value;
      case 8116:
      case 7059:
      case 5753:
      case 5535:
      case 5445:
      case 5701:
      case 4933:
      case 4677:
      case 5533:
      case 5789:
      case 5021:
      case 4765:
        if (strlen(value) - 1 - length2 > 6) switch (charat(value, length2 + 1)) {
          case 109:
            if (charat(value, length2 + 4) !== 45) break;
          case 102:
            return replace(value, /(.+:)(.+)-([^]+)/, "$1" + WEBKIT + "$2-$3$1" + MOZ + (charat(value, length2 + 3) == 108 ? "$3" : "$2-$3")) + value;
          case 115:
            return ~indexof(value, "stretch") ? prefix(replace(value, "stretch", "fill-available"), length2) + value : value;
        }
        break;
      case 4949:
        if (charat(value, length2 + 1) !== 115) break;
      case 6444:
        switch (charat(value, strlen(value) - 3 - (~indexof(value, "!important") && 10))) {
          case 107:
            return replace(value, ":", ":" + WEBKIT) + value;
          case 101:
            return replace(value, /(.+:)([^;!]+)(;|!.+)?/, "$1" + WEBKIT + (charat(value, 14) === 45 ? "inline-" : "") + "box$3$1" + WEBKIT + "$2$3$1" + MS + "$2box$3") + value;
        }
        break;
      case 5936:
        switch (charat(value, length2 + 11)) {
          case 114:
            return WEBKIT + value + MS + replace(value, /[svh]\w+-[tblr]{2}/, "tb") + value;
          case 108:
            return WEBKIT + value + MS + replace(value, /[svh]\w+-[tblr]{2}/, "tb-rl") + value;
          case 45:
            return WEBKIT + value + MS + replace(value, /[svh]\w+-[tblr]{2}/, "lr") + value;
        }
        return WEBKIT + value + MS + value + value;
    }
    return value;
  }
  var prefixer = function prefixer2(element, index2, children, callback) {
    if (element.length > -1) {
      if (!element["return"]) switch (element.type) {
        case DECLARATION:
          element["return"] = prefix(element.value, element.length);
          break;
        case KEYFRAMES:
          return serialize([copy(element, {
            value: replace(element.value, "@", "@" + WEBKIT)
          })], callback);
        case RULESET:
          if (element.length) return combine(element.props, function(value) {
            switch (match(value, /(::plac\w+|:read-\w+)/)) {
              case ":read-only":
              case ":read-write":
                return serialize([copy(element, {
                  props: [replace(value, /:(read-\w+)/, ":" + MOZ + "$1")]
                })], callback);
              case "::placeholder":
                return serialize([copy(element, {
                  props: [replace(value, /:(plac\w+)/, ":" + WEBKIT + "input-$1")]
                }), copy(element, {
                  props: [replace(value, /:(plac\w+)/, ":" + MOZ + "$1")]
                }), copy(element, {
                  props: [replace(value, /:(plac\w+)/, MS + "input-$1")]
                })], callback);
            }
            return "";
          });
      }
    }
  };
  var defaultStylisPlugins = [prefixer];
  var createCache = function createCache2(options2) {
    var key = options2.key;
    if (key === "css") {
      var ssrStyles = document.querySelectorAll("style[data-emotion]:not([data-s])");
      Array.prototype.forEach.call(ssrStyles, function(node2) {
        var dataEmotionAttribute = node2.getAttribute("data-emotion");
        if (dataEmotionAttribute.indexOf(" ") === -1) {
          return;
        }
        document.head.appendChild(node2);
        node2.setAttribute("data-s", "");
      });
    }
    var stylisPlugins = options2.stylisPlugins || defaultStylisPlugins;
    var inserted = {};
    var container;
    var nodesToHydrate = [];
    {
      container = options2.container || document.head;
      Array.prototype.forEach.call(
        // this means we will ignore elements which don't have a space in them which
        // means that the style elements we're looking at are only Emotion 11 server-rendered style elements
        document.querySelectorAll('style[data-emotion^="' + key + ' "]'),
        function(node2) {
          var attrib = node2.getAttribute("data-emotion").split(" ");
          for (var i2 = 1; i2 < attrib.length; i2++) {
            inserted[attrib[i2]] = true;
          }
          nodesToHydrate.push(node2);
        }
      );
    }
    var _insert;
    var omnipresentPlugins = [compat, removeLabel];
    {
      var currentSheet;
      var finalizingPlugins = [stringify, rulesheet(function(rule) {
        currentSheet.insert(rule);
      })];
      var serializer = middleware(omnipresentPlugins.concat(stylisPlugins, finalizingPlugins));
      var stylis = function stylis2(styles) {
        return serialize(compile(styles), serializer);
      };
      _insert = function insert(selector, serialized, sheet, shouldCache) {
        currentSheet = sheet;
        stylis(selector ? selector + "{" + serialized.styles + "}" : serialized.styles);
        if (shouldCache) {
          cache.inserted[serialized.name] = true;
        }
      };
    }
    var cache = {
      key,
      sheet: new StyleSheet({
        key,
        container,
        nonce: options2.nonce,
        speedy: options2.speedy,
        prepend: options2.prepend,
        insertionPoint: options2.insertionPoint
      }),
      nonce: options2.nonce,
      inserted,
      registered: {},
      insert: _insert
    };
    cache.sheet.hydrate(nodesToHydrate);
    return cache;
  };
  var commonjsGlobal = typeof globalThis !== "undefined" ? globalThis : typeof window !== "undefined" ? window : typeof global !== "undefined" ? global : typeof self !== "undefined" ? self : {};
  function getDefaultExportFromCjs(x2) {
    return x2 && x2.__esModule && Object.prototype.hasOwnProperty.call(x2, "default") ? x2["default"] : x2;
  }
  var reactIs$1 = { exports: {} };
  var reactIs_production_min = {};
  /** @license React v16.13.1
   * react-is.production.min.js
   *
   * Copyright (c) Facebook, Inc. and its affiliates.
   *
   * This source code is licensed under the MIT license found in the
   * LICENSE file in the root directory of this source tree.
   */
  var b = "function" === typeof Symbol && Symbol.for, c = b ? Symbol.for("react.element") : 60103, d = b ? Symbol.for("react.portal") : 60106, e = b ? Symbol.for("react.fragment") : 60107, f = b ? Symbol.for("react.strict_mode") : 60108, g = b ? Symbol.for("react.profiler") : 60114, h = b ? Symbol.for("react.provider") : 60109, k = b ? Symbol.for("react.context") : 60110, l = b ? Symbol.for("react.async_mode") : 60111, m = b ? Symbol.for("react.concurrent_mode") : 60111, n = b ? Symbol.for("react.forward_ref") : 60112, p = b ? Symbol.for("react.suspense") : 60113, q = b ? Symbol.for("react.suspense_list") : 60120, r = b ? Symbol.for("react.memo") : 60115, t = b ? Symbol.for("react.lazy") : 60116, v = b ? Symbol.for("react.block") : 60121, w$1 = b ? Symbol.for("react.fundamental") : 60117, x = b ? Symbol.for("react.responder") : 60118, y = b ? Symbol.for("react.scope") : 60119;
  function z(a) {
    if ("object" === typeof a && null !== a) {
      var u = a.$$typeof;
      switch (u) {
        case c:
          switch (a = a.type, a) {
            case l:
            case m:
            case e:
            case g:
            case f:
            case p:
              return a;
            default:
              switch (a = a && a.$$typeof, a) {
                case k:
                case n:
                case t:
                case r:
                case h:
                  return a;
                default:
                  return u;
              }
          }
        case d:
          return u;
      }
    }
  }
  function A(a) {
    return z(a) === m;
  }
  reactIs_production_min.AsyncMode = l;
  reactIs_production_min.ConcurrentMode = m;
  reactIs_production_min.ContextConsumer = k;
  reactIs_production_min.ContextProvider = h;
  reactIs_production_min.Element = c;
  reactIs_production_min.ForwardRef = n;
  reactIs_production_min.Fragment = e;
  reactIs_production_min.Lazy = t;
  reactIs_production_min.Memo = r;
  reactIs_production_min.Portal = d;
  reactIs_production_min.Profiler = g;
  reactIs_production_min.StrictMode = f;
  reactIs_production_min.Suspense = p;
  reactIs_production_min.isAsyncMode = function(a) {
    return A(a) || z(a) === l;
  };
  reactIs_production_min.isConcurrentMode = A;
  reactIs_production_min.isContextConsumer = function(a) {
    return z(a) === k;
  };
  reactIs_production_min.isContextProvider = function(a) {
    return z(a) === h;
  };
  reactIs_production_min.isElement = function(a) {
    return "object" === typeof a && null !== a && a.$$typeof === c;
  };
  reactIs_production_min.isForwardRef = function(a) {
    return z(a) === n;
  };
  reactIs_production_min.isFragment = function(a) {
    return z(a) === e;
  };
  reactIs_production_min.isLazy = function(a) {
    return z(a) === t;
  };
  reactIs_production_min.isMemo = function(a) {
    return z(a) === r;
  };
  reactIs_production_min.isPortal = function(a) {
    return z(a) === d;
  };
  reactIs_production_min.isProfiler = function(a) {
    return z(a) === g;
  };
  reactIs_production_min.isStrictMode = function(a) {
    return z(a) === f;
  };
  reactIs_production_min.isSuspense = function(a) {
    return z(a) === p;
  };
  reactIs_production_min.isValidElementType = function(a) {
    return "string" === typeof a || "function" === typeof a || a === e || a === m || a === g || a === f || a === p || a === q || "object" === typeof a && null !== a && (a.$$typeof === t || a.$$typeof === r || a.$$typeof === h || a.$$typeof === k || a.$$typeof === n || a.$$typeof === w$1 || a.$$typeof === x || a.$$typeof === y || a.$$typeof === v);
  };
  reactIs_production_min.typeOf = z;
  {
    reactIs$1.exports = reactIs_production_min;
  }
  var reactIsExports = reactIs$1.exports;
  var reactIs = reactIsExports;
  var FORWARD_REF_STATICS = {
    "$$typeof": true,
    render: true,
    defaultProps: true,
    displayName: true,
    propTypes: true
  };
  var MEMO_STATICS = {
    "$$typeof": true,
    compare: true,
    defaultProps: true,
    displayName: true,
    propTypes: true,
    type: true
  };
  var TYPE_STATICS = {};
  TYPE_STATICS[reactIs.ForwardRef] = FORWARD_REF_STATICS;
  TYPE_STATICS[reactIs.Memo] = MEMO_STATICS;
  var isBrowser = true;
  function getRegisteredStyles(registered, registeredStyles, classNames2) {
    var rawClassName = "";
    classNames2.split(" ").forEach(function(className) {
      if (registered[className] !== void 0) {
        registeredStyles.push(registered[className] + ";");
      } else if (className) {
        rawClassName += className + " ";
      }
    });
    return rawClassName;
  }
  var registerStyles = function registerStyles2(cache, serialized, isStringTag) {
    var className = cache.key + "-" + serialized.name;
    if (
      // we only need to add the styles to the registered cache if the
      // class name could be used further down
      // the tree but if it's a string tag, we know it won't
      // so we don't have to add it to registered cache.
      // this improves memory usage since we can avoid storing the whole style string
      (isStringTag === false || // we need to always store it if we're in compat mode and
      // in node since emotion-server relies on whether a style is in
      // the registered cache to know whether a style is global or not
      // also, note that this check will be dead code eliminated in the browser
      isBrowser === false) && cache.registered[className] === void 0
    ) {
      cache.registered[className] = serialized.styles;
    }
  };
  var insertStyles = function insertStyles2(cache, serialized, isStringTag) {
    registerStyles(cache, serialized, isStringTag);
    var className = cache.key + "-" + serialized.name;
    if (cache.inserted[serialized.name] === void 0) {
      var current = serialized;
      do {
        cache.insert(serialized === current ? "." + className : "", current, cache.sheet, true);
        current = current.next;
      } while (current !== void 0);
    }
  };
  function murmur2(str) {
    var h2 = 0;
    var k2, i2 = 0, len = str.length;
    for (; len >= 4; ++i2, len -= 4) {
      k2 = str.charCodeAt(i2) & 255 | (str.charCodeAt(++i2) & 255) << 8 | (str.charCodeAt(++i2) & 255) << 16 | (str.charCodeAt(++i2) & 255) << 24;
      k2 = /* Math.imul(k, m): */
      (k2 & 65535) * 1540483477 + ((k2 >>> 16) * 59797 << 16);
      k2 ^= /* k >>> r: */
      k2 >>> 24;
      h2 = /* Math.imul(k, m): */
      (k2 & 65535) * 1540483477 + ((k2 >>> 16) * 59797 << 16) ^ /* Math.imul(h, m): */
      (h2 & 65535) * 1540483477 + ((h2 >>> 16) * 59797 << 16);
    }
    switch (len) {
      case 3:
        h2 ^= (str.charCodeAt(i2 + 2) & 255) << 16;
      case 2:
        h2 ^= (str.charCodeAt(i2 + 1) & 255) << 8;
      case 1:
        h2 ^= str.charCodeAt(i2) & 255;
        h2 = /* Math.imul(h, m): */
        (h2 & 65535) * 1540483477 + ((h2 >>> 16) * 59797 << 16);
    }
    h2 ^= h2 >>> 13;
    h2 = /* Math.imul(h, m): */
    (h2 & 65535) * 1540483477 + ((h2 >>> 16) * 59797 << 16);
    return ((h2 ^ h2 >>> 15) >>> 0).toString(36);
  }
  var unitlessKeys = {
    animationIterationCount: 1,
    aspectRatio: 1,
    borderImageOutset: 1,
    borderImageSlice: 1,
    borderImageWidth: 1,
    boxFlex: 1,
    boxFlexGroup: 1,
    boxOrdinalGroup: 1,
    columnCount: 1,
    columns: 1,
    flex: 1,
    flexGrow: 1,
    flexPositive: 1,
    flexShrink: 1,
    flexNegative: 1,
    flexOrder: 1,
    gridRow: 1,
    gridRowEnd: 1,
    gridRowSpan: 1,
    gridRowStart: 1,
    gridColumn: 1,
    gridColumnEnd: 1,
    gridColumnSpan: 1,
    gridColumnStart: 1,
    msGridRow: 1,
    msGridRowSpan: 1,
    msGridColumn: 1,
    msGridColumnSpan: 1,
    fontWeight: 1,
    lineHeight: 1,
    opacity: 1,
    order: 1,
    orphans: 1,
    scale: 1,
    tabSize: 1,
    widows: 1,
    zIndex: 1,
    zoom: 1,
    WebkitLineClamp: 1,
    // SVG-related properties
    fillOpacity: 1,
    floodOpacity: 1,
    stopOpacity: 1,
    strokeDasharray: 1,
    strokeDashoffset: 1,
    strokeMiterlimit: 1,
    strokeOpacity: 1,
    strokeWidth: 1
  };
  var hyphenateRegex = /[A-Z]|^ms/g;
  var animationRegex = /_EMO_([^_]+?)_([^]*?)_EMO_/g;
  var isCustomProperty = function isCustomProperty2(property) {
    return property.charCodeAt(1) === 45;
  };
  var isProcessableValue = function isProcessableValue2(value) {
    return value != null && typeof value !== "boolean";
  };
  var processStyleName = /* @__PURE__ */ memoize(function(styleName) {
    return isCustomProperty(styleName) ? styleName : styleName.replace(hyphenateRegex, "-$&").toLowerCase();
  });
  var processStyleValue = function processStyleValue2(key, value) {
    switch (key) {
      case "animation":
      case "animationName": {
        if (typeof value === "string") {
          return value.replace(animationRegex, function(match2, p1, p2) {
            cursor = {
              name: p1,
              styles: p2,
              next: cursor
            };
            return p1;
          });
        }
      }
    }
    if (unitlessKeys[key] !== 1 && !isCustomProperty(key) && typeof value === "number" && value !== 0) {
      return value + "px";
    }
    return value;
  };
  function handleInterpolation(mergedProps, registered, interpolation) {
    if (interpolation == null) {
      return "";
    }
    var componentSelector = interpolation;
    if (componentSelector.__emotion_styles !== void 0) {
      return componentSelector;
    }
    switch (typeof interpolation) {
      case "boolean": {
        return "";
      }
      case "object": {
        var keyframes2 = interpolation;
        if (keyframes2.anim === 1) {
          cursor = {
            name: keyframes2.name,
            styles: keyframes2.styles,
            next: cursor
          };
          return keyframes2.name;
        }
        var serializedStyles = interpolation;
        if (serializedStyles.styles !== void 0) {
          var next2 = serializedStyles.next;
          if (next2 !== void 0) {
            while (next2 !== void 0) {
              cursor = {
                name: next2.name,
                styles: next2.styles,
                next: cursor
              };
              next2 = next2.next;
            }
          }
          var styles = serializedStyles.styles + ";";
          return styles;
        }
        return createStringFromObject(mergedProps, registered, interpolation);
      }
      case "function": {
        if (mergedProps !== void 0) {
          var previousCursor = cursor;
          var result = interpolation(mergedProps);
          cursor = previousCursor;
          return handleInterpolation(mergedProps, registered, result);
        }
        break;
      }
    }
    var asString = interpolation;
    {
      return asString;
    }
  }
  function createStringFromObject(mergedProps, registered, obj) {
    var string = "";
    if (Array.isArray(obj)) {
      for (var i2 = 0; i2 < obj.length; i2++) {
        string += handleInterpolation(mergedProps, registered, obj[i2]) + ";";
      }
    } else {
      for (var key in obj) {
        var value = obj[key];
        if (typeof value !== "object") {
          var asString = value;
          if (isProcessableValue(asString)) {
            string += processStyleName(key) + ":" + processStyleValue(key, asString) + ";";
          }
        } else {
          if (Array.isArray(value) && typeof value[0] === "string" && registered == null) {
            for (var _i = 0; _i < value.length; _i++) {
              if (isProcessableValue(value[_i])) {
                string += processStyleName(key) + ":" + processStyleValue(key, value[_i]) + ";";
              }
            }
          } else {
            var interpolated = handleInterpolation(mergedProps, registered, value);
            switch (key) {
              case "animation":
              case "animationName": {
                string += processStyleName(key) + ":" + interpolated + ";";
                break;
              }
              default: {
                string += key + "{" + interpolated + "}";
              }
            }
          }
        }
      }
    }
    return string;
  }
  var labelPattern = /label:\s*([^\s;{]+)\s*(;|$)/g;
  var cursor;
  function serializeStyles(args, registered, mergedProps) {
    if (args.length === 1 && typeof args[0] === "object" && args[0] !== null && args[0].styles !== void 0) {
      return args[0];
    }
    var stringMode = true;
    var styles = "";
    cursor = void 0;
    var strings = args[0];
    if (strings == null || strings.raw === void 0) {
      stringMode = false;
      styles += handleInterpolation(mergedProps, registered, strings);
    } else {
      var asTemplateStringsArr = strings;
      styles += asTemplateStringsArr[0];
    }
    for (var i2 = 1; i2 < args.length; i2++) {
      styles += handleInterpolation(mergedProps, registered, args[i2]);
      if (stringMode) {
        var templateStringsArr = strings;
        styles += templateStringsArr[i2];
      }
    }
    labelPattern.lastIndex = 0;
    var identifierName = "";
    var match2;
    while ((match2 = labelPattern.exec(styles)) !== null) {
      identifierName += "-" + match2[1];
    }
    var name = murmur2(styles) + identifierName;
    return {
      name,
      styles,
      next: cursor
    };
  }
  var syncFallback = function syncFallback2(create) {
    return create();
  };
  var useInsertionEffect = React__namespace["useInsertionEffect"] ? React__namespace["useInsertionEffect"] : false;
  var useInsertionEffectAlwaysWithSyncFallback = useInsertionEffect || syncFallback;
  var EmotionCacheContext = /* @__PURE__ */ React__namespace.createContext(
    // we're doing this to avoid preconstruct's dead code elimination in this one case
    // because this module is primarily intended for the browser and node
    // but it's also required in react native and similar environments sometimes
    // and we could have a special build just for that
    // but this is much easier and the native packages
    // might use a different theme context in the future anyway
    typeof HTMLElement !== "undefined" ? /* @__PURE__ */ createCache({
      key: "css"
    }) : null
  );
  EmotionCacheContext.Provider;
  var withEmotionCache = function withEmotionCache2(func) {
    return /* @__PURE__ */ React.forwardRef(function(props, ref) {
      var cache = React.useContext(EmotionCacheContext);
      return func(props, cache, ref);
    });
  };
  var ThemeContext = /* @__PURE__ */ React__namespace.createContext({});
  var hasOwn = {}.hasOwnProperty;
  var typePropName = "__EMOTION_TYPE_PLEASE_DO_NOT_USE__";
  var createEmotionProps = function createEmotionProps2(type, props) {
    var newProps = {};
    for (var _key in props) {
      if (hasOwn.call(props, _key)) {
        newProps[_key] = props[_key];
      }
    }
    newProps[typePropName] = type;
    return newProps;
  };
  var Insertion = function Insertion2(_ref3) {
    var cache = _ref3.cache, serialized = _ref3.serialized, isStringTag = _ref3.isStringTag;
    registerStyles(cache, serialized, isStringTag);
    useInsertionEffectAlwaysWithSyncFallback(function() {
      return insertStyles(cache, serialized, isStringTag);
    });
    return null;
  };
  var Emotion = /* @__PURE__ */ withEmotionCache(function(props, cache, ref) {
    var cssProp = props.css;
    if (typeof cssProp === "string" && cache.registered[cssProp] !== void 0) {
      cssProp = cache.registered[cssProp];
    }
    var WrappedComponent = props[typePropName];
    var registeredStyles = [cssProp];
    var className = "";
    if (typeof props.className === "string") {
      className = getRegisteredStyles(cache.registered, registeredStyles, props.className);
    } else if (props.className != null) {
      className = props.className + " ";
    }
    var serialized = serializeStyles(registeredStyles, void 0, React__namespace.useContext(ThemeContext));
    className += cache.key + "-" + serialized.name;
    var newProps = {};
    for (var _key2 in props) {
      if (hasOwn.call(props, _key2) && _key2 !== "css" && _key2 !== typePropName && true) {
        newProps[_key2] = props[_key2];
      }
    }
    newProps.className = className;
    if (ref) {
      newProps.ref = ref;
    }
    return /* @__PURE__ */ React__namespace.createElement(React__namespace.Fragment, null, /* @__PURE__ */ React__namespace.createElement(Insertion, {
      cache,
      serialized,
      isStringTag: typeof WrappedComponent === "string"
    }), /* @__PURE__ */ React__namespace.createElement(WrappedComponent, newProps));
  });
  var Emotion$1 = Emotion;
  var jsx = function jsx2(type, props) {
    var args = arguments;
    if (props == null || !hasOwn.call(props, "css")) {
      return React__namespace.createElement.apply(void 0, args);
    }
    var argsLength = args.length;
    var createElementArgArray = new Array(argsLength);
    createElementArgArray[0] = Emotion$1;
    createElementArgArray[1] = createEmotionProps(type, props);
    for (var i2 = 2; i2 < argsLength; i2++) {
      createElementArgArray[i2] = args[i2];
    }
    return React__namespace.createElement.apply(null, createElementArgArray);
  };
  (function(_jsx) {
    var JSX;
    /* @__PURE__ */ (function(_JSX) {
    })(JSX || (JSX = _jsx.JSX || (_jsx.JSX = {})));
  })(jsx || (jsx = {}));
  function css() {
    for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }
    return serializeStyles(args);
  }
  function keyframes() {
    var insertable = css.apply(void 0, arguments);
    var name = "animation-" + insertable.name;
    return {
      name,
      styles: "@keyframes " + name + "{" + insertable.styles + "}",
      anim: 1,
      toString: function toString() {
        return "_EMO_" + this.name + "_" + this.styles + "_EMO_";
      }
    };
  }
  function _taggedTemplateLiteral(e2, t2) {
    return t2 || (t2 = e2.slice(0)), Object.freeze(Object.defineProperties(e2, {
      raw: {
        value: Object.freeze(t2)
      }
    }));
  }
  const min = Math.min;
  const max = Math.max;
  const round = Math.round;
  const floor = Math.floor;
  const createCoords = (v2) => ({
    x: v2,
    y: v2
  });
  function rectToClientRect(rect) {
    const {
      x: x2,
      y: y2,
      width,
      height
    } = rect;
    return {
      width,
      height,
      top: y2,
      left: x2,
      right: x2 + width,
      bottom: y2 + height,
      x: x2,
      y: y2
    };
  }
  function hasWindow() {
    return typeof window !== "undefined";
  }
  function getNodeName(node2) {
    if (isNode(node2)) {
      return (node2.nodeName || "").toLowerCase();
    }
    return "#document";
  }
  function getWindow(node2) {
    var _node$ownerDocument;
    return (node2 == null || (_node$ownerDocument = node2.ownerDocument) == null ? void 0 : _node$ownerDocument.defaultView) || window;
  }
  function getDocumentElement(node2) {
    var _ref3;
    return (_ref3 = (isNode(node2) ? node2.ownerDocument : node2.document) || window.document) == null ? void 0 : _ref3.documentElement;
  }
  function isNode(value) {
    if (!hasWindow()) {
      return false;
    }
    return value instanceof Node || value instanceof getWindow(value).Node;
  }
  function isElement(value) {
    if (!hasWindow()) {
      return false;
    }
    return value instanceof Element || value instanceof getWindow(value).Element;
  }
  function isHTMLElement(value) {
    if (!hasWindow()) {
      return false;
    }
    return value instanceof HTMLElement || value instanceof getWindow(value).HTMLElement;
  }
  function isShadowRoot(value) {
    if (!hasWindow() || typeof ShadowRoot === "undefined") {
      return false;
    }
    return value instanceof ShadowRoot || value instanceof getWindow(value).ShadowRoot;
  }
  function isOverflowElement(element) {
    const {
      overflow,
      overflowX,
      overflowY,
      display
    } = getComputedStyle$1(element);
    return /auto|scroll|overlay|hidden|clip/.test(overflow + overflowY + overflowX) && display !== "inline" && display !== "contents";
  }
  let isWebKitValue;
  function isWebKit() {
    if (isWebKitValue == null) {
      isWebKitValue = typeof CSS !== "undefined" && CSS.supports && CSS.supports("-webkit-backdrop-filter", "none");
    }
    return isWebKitValue;
  }
  function isLastTraversableNode(node2) {
    return /^(html|body|#document)$/.test(getNodeName(node2));
  }
  function getComputedStyle$1(element) {
    return getWindow(element).getComputedStyle(element);
  }
  function getParentNode(node2) {
    if (getNodeName(node2) === "html") {
      return node2;
    }
    const result = (
      // Step into the shadow DOM of the parent of a slotted node.
      node2.assignedSlot || // DOM Element detected.
      node2.parentNode || // ShadowRoot detected.
      isShadowRoot(node2) && node2.host || // Fallback.
      getDocumentElement(node2)
    );
    return isShadowRoot(result) ? result.host : result;
  }
  function getNearestOverflowAncestor(node2) {
    const parentNode = getParentNode(node2);
    if (isLastTraversableNode(parentNode)) {
      return node2.ownerDocument ? node2.ownerDocument.body : node2.body;
    }
    if (isHTMLElement(parentNode) && isOverflowElement(parentNode)) {
      return parentNode;
    }
    return getNearestOverflowAncestor(parentNode);
  }
  function getOverflowAncestors(node2, list, traverseIframes) {
    var _node$ownerDocument2;
    if (list === void 0) {
      list = [];
    }
    if (traverseIframes === void 0) {
      traverseIframes = true;
    }
    const scrollableAncestor = getNearestOverflowAncestor(node2);
    const isBody = scrollableAncestor === ((_node$ownerDocument2 = node2.ownerDocument) == null ? void 0 : _node$ownerDocument2.body);
    const win2 = getWindow(scrollableAncestor);
    if (isBody) {
      const frameElement = getFrameElement(win2);
      return list.concat(win2, win2.visualViewport || [], isOverflowElement(scrollableAncestor) ? scrollableAncestor : [], frameElement && traverseIframes ? getOverflowAncestors(frameElement) : []);
    } else {
      return list.concat(scrollableAncestor, getOverflowAncestors(scrollableAncestor, [], traverseIframes));
    }
  }
  function getFrameElement(win2) {
    return win2.parent && Object.getPrototypeOf(win2.parent) ? win2.frameElement : null;
  }
  function getCssDimensions(element) {
    const css3 = getComputedStyle$1(element);
    let width = parseFloat(css3.width) || 0;
    let height = parseFloat(css3.height) || 0;
    const hasOffset = isHTMLElement(element);
    const offsetWidth = hasOffset ? element.offsetWidth : width;
    const offsetHeight = hasOffset ? element.offsetHeight : height;
    const shouldFallback = round(width) !== offsetWidth || round(height) !== offsetHeight;
    if (shouldFallback) {
      width = offsetWidth;
      height = offsetHeight;
    }
    return {
      width,
      height,
      $: shouldFallback
    };
  }
  function unwrapElement(element) {
    return !isElement(element) ? element.contextElement : element;
  }
  function getScale(element) {
    const domElement = unwrapElement(element);
    if (!isHTMLElement(domElement)) {
      return createCoords(1);
    }
    const rect = domElement.getBoundingClientRect();
    const {
      width,
      height,
      $
    } = getCssDimensions(domElement);
    let x2 = ($ ? round(rect.width) : rect.width) / width;
    let y2 = ($ ? round(rect.height) : rect.height) / height;
    if (!x2 || !Number.isFinite(x2)) {
      x2 = 1;
    }
    if (!y2 || !Number.isFinite(y2)) {
      y2 = 1;
    }
    return {
      x: x2,
      y: y2
    };
  }
  const noOffsets = /* @__PURE__ */ createCoords(0);
  function getVisualOffsets(element) {
    const win2 = getWindow(element);
    if (!isWebKit() || !win2.visualViewport) {
      return noOffsets;
    }
    return {
      x: win2.visualViewport.offsetLeft,
      y: win2.visualViewport.offsetTop
    };
  }
  function shouldAddVisualOffsets(element, isFixed, floatingOffsetParent) {
    {
      return false;
    }
  }
  function getBoundingClientRect(element, includeScale, isFixedStrategy, offsetParent) {
    if (includeScale === void 0) {
      includeScale = false;
    }
    const clientRect = element.getBoundingClientRect();
    const domElement = unwrapElement(element);
    let scale = createCoords(1);
    if (includeScale) {
      {
        scale = getScale(element);
      }
    }
    const visualOffsets = shouldAddVisualOffsets() ? getVisualOffsets(domElement) : createCoords(0);
    let x2 = (clientRect.left + visualOffsets.x) / scale.x;
    let y2 = (clientRect.top + visualOffsets.y) / scale.y;
    let width = clientRect.width / scale.x;
    let height = clientRect.height / scale.y;
    if (domElement) {
      const win2 = getWindow(domElement);
      const offsetWin = offsetParent;
      let currentWin = win2;
      let currentIFrame = getFrameElement(currentWin);
      while (currentIFrame && offsetParent && offsetWin !== currentWin) {
        const iframeScale = getScale(currentIFrame);
        const iframeRect = currentIFrame.getBoundingClientRect();
        const css3 = getComputedStyle$1(currentIFrame);
        const left = iframeRect.left + (currentIFrame.clientLeft + parseFloat(css3.paddingLeft)) * iframeScale.x;
        const top = iframeRect.top + (currentIFrame.clientTop + parseFloat(css3.paddingTop)) * iframeScale.y;
        x2 *= iframeScale.x;
        y2 *= iframeScale.y;
        width *= iframeScale.x;
        height *= iframeScale.y;
        x2 += left;
        y2 += top;
        currentWin = getWindow(currentIFrame);
        currentIFrame = getFrameElement(currentWin);
      }
    }
    return rectToClientRect({
      width,
      height,
      x: x2,
      y: y2
    });
  }
  function rectsAreEqual(a, b2) {
    return a.x === b2.x && a.y === b2.y && a.width === b2.width && a.height === b2.height;
  }
  function observeMove(element, onMove) {
    let io = null;
    let timeoutId;
    const root = getDocumentElement(element);
    function cleanup() {
      var _io;
      clearTimeout(timeoutId);
      (_io = io) == null || _io.disconnect();
      io = null;
    }
    function refresh(skip, threshold) {
      if (skip === void 0) {
        skip = false;
      }
      if (threshold === void 0) {
        threshold = 1;
      }
      cleanup();
      const elementRectForRootMargin = element.getBoundingClientRect();
      const {
        left,
        top,
        width,
        height
      } = elementRectForRootMargin;
      if (!skip) {
        onMove();
      }
      if (!width || !height) {
        return;
      }
      const insetTop = floor(top);
      const insetRight = floor(root.clientWidth - (left + width));
      const insetBottom = floor(root.clientHeight - (top + height));
      const insetLeft = floor(left);
      const rootMargin = -insetTop + "px " + -insetRight + "px " + -insetBottom + "px " + -insetLeft + "px";
      const options2 = {
        rootMargin,
        threshold: max(0, min(1, threshold)) || 1
      };
      let isFirstUpdate = true;
      function handleObserve(entries) {
        const ratio = entries[0].intersectionRatio;
        if (ratio !== threshold) {
          if (!isFirstUpdate) {
            return refresh();
          }
          if (!ratio) {
            timeoutId = setTimeout(() => {
              refresh(false, 1e-7);
            }, 1e3);
          } else {
            refresh(false, ratio);
          }
        }
        if (ratio === 1 && !rectsAreEqual(elementRectForRootMargin, element.getBoundingClientRect())) {
          refresh();
        }
        isFirstUpdate = false;
      }
      try {
        io = new IntersectionObserver(handleObserve, __spreadProps(__spreadValues({}, options2), {
          // Handle <iframe>s
          root: root.ownerDocument
        }));
      } catch (_e) {
        io = new IntersectionObserver(handleObserve, options2);
      }
      io.observe(element);
    }
    refresh(true);
    return cleanup;
  }
  function autoUpdate(reference, floating, update, options2) {
    if (options2 === void 0) {
      options2 = {};
    }
    const {
      ancestorScroll = true,
      ancestorResize = true,
      elementResize = typeof ResizeObserver === "function",
      layoutShift = typeof IntersectionObserver === "function",
      animationFrame = false
    } = options2;
    const referenceEl = unwrapElement(reference);
    const ancestors = ancestorScroll || ancestorResize ? [...referenceEl ? getOverflowAncestors(referenceEl) : [], ...floating ? getOverflowAncestors(floating) : []] : [];
    ancestors.forEach((ancestor) => {
      ancestorScroll && ancestor.addEventListener("scroll", update, {
        passive: true
      });
      ancestorResize && ancestor.addEventListener("resize", update);
    });
    const cleanupIo = referenceEl && layoutShift ? observeMove(referenceEl, update) : null;
    let reobserveFrame = -1;
    let resizeObserver = null;
    if (elementResize) {
      resizeObserver = new ResizeObserver((_ref3) => {
        let [firstEntry] = _ref3;
        if (firstEntry && firstEntry.target === referenceEl && resizeObserver && floating) {
          resizeObserver.unobserve(floating);
          cancelAnimationFrame(reobserveFrame);
          reobserveFrame = requestAnimationFrame(() => {
            var _resizeObserver;
            (_resizeObserver = resizeObserver) == null || _resizeObserver.observe(floating);
          });
        }
        update();
      });
      if (referenceEl && !animationFrame) {
        resizeObserver.observe(referenceEl);
      }
      if (floating) {
        resizeObserver.observe(floating);
      }
    }
    let frameId;
    let prevRefRect = animationFrame ? getBoundingClientRect(reference) : null;
    if (animationFrame) {
      frameLoop();
    }
    function frameLoop() {
      const nextRefRect = getBoundingClientRect(reference);
      if (prevRefRect && !rectsAreEqual(prevRefRect, nextRefRect)) {
        update();
      }
      prevRefRect = nextRefRect;
      frameId = requestAnimationFrame(frameLoop);
    }
    update();
    return () => {
      var _resizeObserver2;
      ancestors.forEach((ancestor) => {
        ancestorScroll && ancestor.removeEventListener("scroll", update);
        ancestorResize && ancestor.removeEventListener("resize", update);
      });
      cleanupIo == null || cleanupIo();
      (_resizeObserver2 = resizeObserver) == null || _resizeObserver2.disconnect();
      resizeObserver = null;
      if (animationFrame) {
        cancelAnimationFrame(frameId);
      }
    };
  }
  var index = React.useLayoutEffect;
  var _excluded$4 = ["className", "clearValue", "cx", "getStyles", "getClassNames", "getValue", "hasValue", "isMulti", "isRtl", "options", "selectOption", "selectProps", "setValue", "theme"];
  var noop = function noop2() {
  };
  function applyPrefixToName(prefix2, name) {
    if (!name) {
      return prefix2;
    } else if (name[0] === "-") {
      return prefix2 + name;
    } else {
      return prefix2 + "__" + name;
    }
  }
  function classNames(prefix2, state) {
    for (var _len = arguments.length, classNameList = new Array(_len > 2 ? _len - 2 : 0), _key = 2; _key < _len; _key++) {
      classNameList[_key - 2] = arguments[_key];
    }
    var arr = [].concat(classNameList);
    if (state && prefix2) {
      for (var key in state) {
        if (state.hasOwnProperty(key) && state[key]) {
          arr.push("".concat(applyPrefixToName(prefix2, key)));
        }
      }
    }
    return arr.filter(function(i2) {
      return i2;
    }).map(function(i2) {
      return String(i2).trim();
    }).join(" ");
  }
  var cleanValue = function cleanValue2(value) {
    if (isArray(value)) return value.filter(Boolean);
    if (_typeof(value) === "object" && value !== null) return [value];
    return [];
  };
  var cleanCommonProps = function cleanCommonProps2(props) {
    props.className;
    props.clearValue;
    props.cx;
    props.getStyles;
    props.getClassNames;
    props.getValue;
    props.hasValue;
    props.isMulti;
    props.isRtl;
    props.options;
    props.selectOption;
    props.selectProps;
    props.setValue;
    props.theme;
    var innerProps = _objectWithoutProperties(props, _excluded$4);
    return _objectSpread2({}, innerProps);
  };
  var getStyleProps = function getStyleProps2(props, name, classNamesState) {
    var cx = props.cx, getStyles = props.getStyles, getClassNames = props.getClassNames, className = props.className;
    return {
      css: getStyles(name, props),
      className: cx(classNamesState !== null && classNamesState !== void 0 ? classNamesState : {}, getClassNames(name, props), className)
    };
  };
  function isDocumentElement(el) {
    return [document.documentElement, document.body, window].indexOf(el) > -1;
  }
  function normalizedHeight(el) {
    if (isDocumentElement(el)) {
      return window.innerHeight;
    }
    return el.clientHeight;
  }
  function getScrollTop(el) {
    if (isDocumentElement(el)) {
      return window.pageYOffset;
    }
    return el.scrollTop;
  }
  function scrollTo(el, top) {
    if (isDocumentElement(el)) {
      window.scrollTo(0, top);
      return;
    }
    el.scrollTop = top;
  }
  function getScrollParent(element) {
    var style = getComputedStyle(element);
    var excludeStaticParent = style.position === "absolute";
    var overflowRx = /(auto|scroll)/;
    if (style.position === "fixed") return document.documentElement;
    for (var parent = element; parent = parent.parentElement; ) {
      style = getComputedStyle(parent);
      if (excludeStaticParent && style.position === "static") {
        continue;
      }
      if (overflowRx.test(style.overflow + style.overflowY + style.overflowX)) {
        return parent;
      }
    }
    return document.documentElement;
  }
  function easeOutCubic(t2, b2, c2, d2) {
    return c2 * ((t2 = t2 / d2 - 1) * t2 * t2 + 1) + b2;
  }
  function animatedScrollTo(element, to) {
    var duration = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : 200;
    var callback = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : noop;
    var start = getScrollTop(element);
    var change = to - start;
    var increment = 10;
    var currentTime = 0;
    function animateScroll() {
      currentTime += increment;
      var val = easeOutCubic(currentTime, start, change, duration);
      scrollTo(element, val);
      if (currentTime < duration) {
        window.requestAnimationFrame(animateScroll);
      } else {
        callback(element);
      }
    }
    animateScroll();
  }
  function scrollIntoView(menuEl, focusedEl) {
    var menuRect = menuEl.getBoundingClientRect();
    var focusedRect = focusedEl.getBoundingClientRect();
    var overScroll = focusedEl.offsetHeight / 3;
    if (focusedRect.bottom + overScroll > menuRect.bottom) {
      scrollTo(menuEl, Math.min(focusedEl.offsetTop + focusedEl.clientHeight - menuEl.offsetHeight + overScroll, menuEl.scrollHeight));
    } else if (focusedRect.top - overScroll < menuRect.top) {
      scrollTo(menuEl, Math.max(focusedEl.offsetTop - overScroll, 0));
    }
  }
  function getBoundingClientObj(element) {
    var rect = element.getBoundingClientRect();
    return {
      bottom: rect.bottom,
      height: rect.height,
      left: rect.left,
      right: rect.right,
      top: rect.top,
      width: rect.width
    };
  }
  function isTouchCapable() {
    try {
      document.createEvent("TouchEvent");
      return true;
    } catch (e2) {
      return false;
    }
  }
  function isMobileDevice() {
    try {
      return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    } catch (e2) {
      return false;
    }
  }
  var passiveOptionAccessed = false;
  var options = {
    get passive() {
      return passiveOptionAccessed = true;
    }
  };
  var w = typeof window !== "undefined" ? window : {};
  if (w.addEventListener && w.removeEventListener) {
    w.addEventListener("p", noop, options);
    w.removeEventListener("p", noop, false);
  }
  var supportsPassiveEvents = passiveOptionAccessed;
  function notNullish(item) {
    return item != null;
  }
  function isArray(arg) {
    return Array.isArray(arg);
  }
  function valueTernary(isMulti, multiValue, singleValue) {
    return isMulti ? multiValue : singleValue;
  }
  function singleValueAsValue(singleValue) {
    return singleValue;
  }
  function multiValueAsValue(multiValue) {
    return multiValue;
  }
  var removeProps = function removeProps2(propsObj) {
    for (var _len2 = arguments.length, properties = new Array(_len2 > 1 ? _len2 - 1 : 0), _key2 = 1; _key2 < _len2; _key2++) {
      properties[_key2 - 1] = arguments[_key2];
    }
    var propsMap = Object.entries(propsObj).filter(function(_ref3) {
      var _ref22 = _slicedToArray(_ref3, 1), key = _ref22[0];
      return !properties.includes(key);
    });
    return propsMap.reduce(function(newProps, _ref3) {
      var _ref4 = _slicedToArray(_ref3, 2), key = _ref4[0], val = _ref4[1];
      newProps[key] = val;
      return newProps;
    }, {});
  };
  var _excluded$3 = ["children", "innerProps"], _excluded2$1 = ["children", "innerProps"];
  function getMenuPlacement(_ref3) {
    var preferredMaxHeight = _ref3.maxHeight, menuEl = _ref3.menuEl, minHeight = _ref3.minHeight, preferredPlacement = _ref3.placement, shouldScroll = _ref3.shouldScroll, isFixedPosition = _ref3.isFixedPosition, controlHeight2 = _ref3.controlHeight;
    var scrollParent = getScrollParent(menuEl);
    var defaultState = {
      placement: "bottom",
      maxHeight: preferredMaxHeight
    };
    if (!menuEl || !menuEl.offsetParent) return defaultState;
    var _scrollParent$getBoun = scrollParent.getBoundingClientRect(), scrollHeight = _scrollParent$getBoun.height;
    var _menuEl$getBoundingCl = menuEl.getBoundingClientRect(), menuBottom = _menuEl$getBoundingCl.bottom, menuHeight = _menuEl$getBoundingCl.height, menuTop = _menuEl$getBoundingCl.top;
    var _menuEl$offsetParent$ = menuEl.offsetParent.getBoundingClientRect(), containerTop = _menuEl$offsetParent$.top;
    var viewHeight = isFixedPosition ? window.innerHeight : normalizedHeight(scrollParent);
    var scrollTop = getScrollTop(scrollParent);
    var marginBottom = parseInt(getComputedStyle(menuEl).marginBottom, 10);
    var marginTop = parseInt(getComputedStyle(menuEl).marginTop, 10);
    var viewSpaceAbove = containerTop - marginTop;
    var viewSpaceBelow = viewHeight - menuTop;
    var scrollSpaceAbove = viewSpaceAbove + scrollTop;
    var scrollSpaceBelow = scrollHeight - scrollTop - menuTop;
    var scrollDown = menuBottom - viewHeight + scrollTop + marginBottom;
    var scrollUp = scrollTop + menuTop - marginTop;
    var scrollDuration = 160;
    switch (preferredPlacement) {
      case "auto":
      case "bottom":
        if (viewSpaceBelow >= menuHeight) {
          return {
            placement: "bottom",
            maxHeight: preferredMaxHeight
          };
        }
        if (scrollSpaceBelow >= menuHeight && !isFixedPosition) {
          if (shouldScroll) {
            animatedScrollTo(scrollParent, scrollDown, scrollDuration);
          }
          return {
            placement: "bottom",
            maxHeight: preferredMaxHeight
          };
        }
        if (!isFixedPosition && scrollSpaceBelow >= minHeight || isFixedPosition && viewSpaceBelow >= minHeight) {
          if (shouldScroll) {
            animatedScrollTo(scrollParent, scrollDown, scrollDuration);
          }
          var constrainedHeight = isFixedPosition ? viewSpaceBelow - marginBottom : scrollSpaceBelow - marginBottom;
          return {
            placement: "bottom",
            maxHeight: constrainedHeight
          };
        }
        if (preferredPlacement === "auto" || isFixedPosition) {
          var _constrainedHeight = preferredMaxHeight;
          var spaceAbove = isFixedPosition ? viewSpaceAbove : scrollSpaceAbove;
          if (spaceAbove >= minHeight) {
            _constrainedHeight = Math.min(spaceAbove - marginBottom - controlHeight2, preferredMaxHeight);
          }
          return {
            placement: "top",
            maxHeight: _constrainedHeight
          };
        }
        if (preferredPlacement === "bottom") {
          if (shouldScroll) {
            scrollTo(scrollParent, scrollDown);
          }
          return {
            placement: "bottom",
            maxHeight: preferredMaxHeight
          };
        }
        break;
      case "top":
        if (viewSpaceAbove >= menuHeight) {
          return {
            placement: "top",
            maxHeight: preferredMaxHeight
          };
        }
        if (scrollSpaceAbove >= menuHeight && !isFixedPosition) {
          if (shouldScroll) {
            animatedScrollTo(scrollParent, scrollUp, scrollDuration);
          }
          return {
            placement: "top",
            maxHeight: preferredMaxHeight
          };
        }
        if (!isFixedPosition && scrollSpaceAbove >= minHeight || isFixedPosition && viewSpaceAbove >= minHeight) {
          var _constrainedHeight2 = preferredMaxHeight;
          if (!isFixedPosition && scrollSpaceAbove >= minHeight || isFixedPosition && viewSpaceAbove >= minHeight) {
            _constrainedHeight2 = isFixedPosition ? viewSpaceAbove - marginTop : scrollSpaceAbove - marginTop;
          }
          if (shouldScroll) {
            animatedScrollTo(scrollParent, scrollUp, scrollDuration);
          }
          return {
            placement: "top",
            maxHeight: _constrainedHeight2
          };
        }
        return {
          placement: "bottom",
          maxHeight: preferredMaxHeight
        };
      default:
        throw new Error('Invalid placement provided "'.concat(preferredPlacement, '".'));
    }
    return defaultState;
  }
  function alignToControl(placement) {
    var placementToCSSProp = {
      bottom: "top",
      top: "bottom"
    };
    return placement ? placementToCSSProp[placement] : "bottom";
  }
  var coercePlacement = function coercePlacement2(p2) {
    return p2 === "auto" ? "bottom" : p2;
  };
  var menuCSS = function menuCSS2(_ref22, unstyled) {
    var _objectSpread2$1;
    var placement = _ref22.placement, _ref2$theme = _ref22.theme, borderRadius2 = _ref2$theme.borderRadius, spacing2 = _ref2$theme.spacing, colors2 = _ref2$theme.colors;
    return _objectSpread2((_objectSpread2$1 = {
      label: "menu"
    }, _defineProperty(_objectSpread2$1, alignToControl(placement), "100%"), _defineProperty(_objectSpread2$1, "position", "absolute"), _defineProperty(_objectSpread2$1, "width", "100%"), _defineProperty(_objectSpread2$1, "zIndex", 1), _objectSpread2$1), unstyled ? {} : {
      backgroundColor: colors2.neutral0,
      borderRadius: borderRadius2,
      boxShadow: "0 0 0 1px hsla(0, 0%, 0%, 0.1), 0 4px 11px hsla(0, 0%, 0%, 0.1)",
      marginBottom: spacing2.menuGutter,
      marginTop: spacing2.menuGutter
    });
  };
  var PortalPlacementContext = /* @__PURE__ */ React.createContext(null);
  var MenuPlacer = function MenuPlacer2(props) {
    var children = props.children, minMenuHeight = props.minMenuHeight, maxMenuHeight = props.maxMenuHeight, menuPlacement = props.menuPlacement, menuPosition = props.menuPosition, menuShouldScrollIntoView = props.menuShouldScrollIntoView, theme = props.theme;
    var _ref3 = React.useContext(PortalPlacementContext) || {}, setPortalPlacement = _ref3.setPortalPlacement;
    var ref = React.useRef(null);
    var _useState = React.useState(maxMenuHeight), _useState2 = _slicedToArray(_useState, 2), maxHeight = _useState2[0], setMaxHeight = _useState2[1];
    var _useState3 = React.useState(null), _useState4 = _slicedToArray(_useState3, 2), placement = _useState4[0], setPlacement = _useState4[1];
    var controlHeight2 = theme.spacing.controlHeight;
    index(function() {
      var menuEl = ref.current;
      if (!menuEl) return;
      var isFixedPosition = menuPosition === "fixed";
      var shouldScroll = menuShouldScrollIntoView && !isFixedPosition;
      var state = getMenuPlacement({
        maxHeight: maxMenuHeight,
        menuEl,
        minHeight: minMenuHeight,
        placement: menuPlacement,
        shouldScroll,
        isFixedPosition,
        controlHeight: controlHeight2
      });
      setMaxHeight(state.maxHeight);
      setPlacement(state.placement);
      setPortalPlacement === null || setPortalPlacement === void 0 ? void 0 : setPortalPlacement(state.placement);
    }, [maxMenuHeight, menuPlacement, menuPosition, menuShouldScrollIntoView, minMenuHeight, setPortalPlacement, controlHeight2]);
    return children({
      ref,
      placerProps: _objectSpread2(_objectSpread2({}, props), {}, {
        placement: placement || coercePlacement(menuPlacement),
        maxHeight
      })
    });
  };
  var Menu = function Menu2(props) {
    var children = props.children, innerRef = props.innerRef, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "menu", {
      menu: true
    }), {
      ref: innerRef
    }, innerProps), children);
  };
  var Menu$1 = Menu;
  var menuListCSS = function menuListCSS2(_ref4, unstyled) {
    var maxHeight = _ref4.maxHeight, baseUnit2 = _ref4.theme.spacing.baseUnit;
    return _objectSpread2({
      maxHeight,
      overflowY: "auto",
      position: "relative",
      // required for offset[Height, Top] > keyboard scroll
      WebkitOverflowScrolling: "touch"
    }, unstyled ? {} : {
      paddingBottom: baseUnit2,
      paddingTop: baseUnit2
    });
  };
  var MenuList = function MenuList2(props) {
    var children = props.children, innerProps = props.innerProps, innerRef = props.innerRef, isMulti = props.isMulti;
    return jsx("div", _extends({}, getStyleProps(props, "menuList", {
      "menu-list": true,
      "menu-list--is-multi": isMulti
    }), {
      ref: innerRef
    }, innerProps), children);
  };
  var noticeCSS = function noticeCSS2(_ref5, unstyled) {
    var _ref5$theme = _ref5.theme, baseUnit2 = _ref5$theme.spacing.baseUnit, colors2 = _ref5$theme.colors;
    return _objectSpread2({
      textAlign: "center"
    }, unstyled ? {} : {
      color: colors2.neutral40,
      padding: "".concat(baseUnit2 * 2, "px ").concat(baseUnit2 * 3, "px")
    });
  };
  var noOptionsMessageCSS = noticeCSS;
  var loadingMessageCSS = noticeCSS;
  var NoOptionsMessage = function NoOptionsMessage2(_ref6) {
    var _ref6$children = _ref6.children, children = _ref6$children === void 0 ? "No options" : _ref6$children, innerProps = _ref6.innerProps, restProps = _objectWithoutProperties(_ref6, _excluded$3);
    return jsx("div", _extends({}, getStyleProps(_objectSpread2(_objectSpread2({}, restProps), {}, {
      children,
      innerProps
    }), "noOptionsMessage", {
      "menu-notice": true,
      "menu-notice--no-options": true
    }), innerProps), children);
  };
  var LoadingMessage = function LoadingMessage2(_ref7) {
    var _ref7$children = _ref7.children, children = _ref7$children === void 0 ? "Loading..." : _ref7$children, innerProps = _ref7.innerProps, restProps = _objectWithoutProperties(_ref7, _excluded2$1);
    return jsx("div", _extends({}, getStyleProps(_objectSpread2(_objectSpread2({}, restProps), {}, {
      children,
      innerProps
    }), "loadingMessage", {
      "menu-notice": true,
      "menu-notice--loading": true
    }), innerProps), children);
  };
  var menuPortalCSS = function menuPortalCSS2(_ref8) {
    var rect = _ref8.rect, offset = _ref8.offset, position2 = _ref8.position;
    return {
      left: rect.left,
      position: position2,
      top: offset,
      width: rect.width,
      zIndex: 1
    };
  };
  var MenuPortal = function MenuPortal2(props) {
    var appendTo = props.appendTo, children = props.children, controlElement = props.controlElement, innerProps = props.innerProps, menuPlacement = props.menuPlacement, menuPosition = props.menuPosition;
    var menuPortalRef = React.useRef(null);
    var cleanupRef = React.useRef(null);
    var _useState5 = React.useState(coercePlacement(menuPlacement)), _useState6 = _slicedToArray(_useState5, 2), placement = _useState6[0], setPortalPlacement = _useState6[1];
    var portalPlacementContext = React.useMemo(function() {
      return {
        setPortalPlacement
      };
    }, []);
    var _useState7 = React.useState(null), _useState8 = _slicedToArray(_useState7, 2), computedPosition = _useState8[0], setComputedPosition = _useState8[1];
    var updateComputedPosition = React.useCallback(function() {
      if (!controlElement) return;
      var rect = getBoundingClientObj(controlElement);
      var scrollDistance = menuPosition === "fixed" ? 0 : window.pageYOffset;
      var offset = rect[placement] + scrollDistance;
      if (offset !== (computedPosition === null || computedPosition === void 0 ? void 0 : computedPosition.offset) || rect.left !== (computedPosition === null || computedPosition === void 0 ? void 0 : computedPosition.rect.left) || rect.width !== (computedPosition === null || computedPosition === void 0 ? void 0 : computedPosition.rect.width)) {
        setComputedPosition({
          offset,
          rect
        });
      }
    }, [controlElement, menuPosition, placement, computedPosition === null || computedPosition === void 0 ? void 0 : computedPosition.offset, computedPosition === null || computedPosition === void 0 ? void 0 : computedPosition.rect.left, computedPosition === null || computedPosition === void 0 ? void 0 : computedPosition.rect.width]);
    index(function() {
      updateComputedPosition();
    }, [updateComputedPosition]);
    var runAutoUpdate = React.useCallback(function() {
      if (typeof cleanupRef.current === "function") {
        cleanupRef.current();
        cleanupRef.current = null;
      }
      if (controlElement && menuPortalRef.current) {
        cleanupRef.current = autoUpdate(controlElement, menuPortalRef.current, updateComputedPosition, {
          elementResize: "ResizeObserver" in window
        });
      }
    }, [controlElement, updateComputedPosition]);
    index(function() {
      runAutoUpdate();
    }, [runAutoUpdate]);
    var setMenuPortalElement = React.useCallback(function(menuPortalElement) {
      menuPortalRef.current = menuPortalElement;
      runAutoUpdate();
    }, [runAutoUpdate]);
    if (!appendTo && menuPosition !== "fixed" || !computedPosition) return null;
    var menuWrapper = jsx("div", _extends({
      ref: setMenuPortalElement
    }, getStyleProps(_objectSpread2(_objectSpread2({}, props), {}, {
      offset: computedPosition.offset,
      position: menuPosition,
      rect: computedPosition.rect
    }), "menuPortal", {
      "menu-portal": true
    }), innerProps), children);
    return jsx(PortalPlacementContext.Provider, {
      value: portalPlacementContext
    }, appendTo ? /* @__PURE__ */ reactDom.createPortal(menuWrapper, appendTo) : menuWrapper);
  };
  var containerCSS = function containerCSS2(_ref3) {
    var isDisabled = _ref3.isDisabled, isRtl = _ref3.isRtl;
    return {
      label: "container",
      direction: isRtl ? "rtl" : void 0,
      pointerEvents: isDisabled ? "none" : void 0,
      // cancel mouse events when disabled
      position: "relative"
    };
  };
  var SelectContainer = function SelectContainer2(props) {
    var children = props.children, innerProps = props.innerProps, isDisabled = props.isDisabled, isRtl = props.isRtl;
    return jsx("div", _extends({}, getStyleProps(props, "container", {
      "--is-disabled": isDisabled,
      "--is-rtl": isRtl
    }), innerProps), children);
  };
  var valueContainerCSS = function valueContainerCSS2(_ref22, unstyled) {
    var spacing2 = _ref22.theme.spacing, isMulti = _ref22.isMulti, hasValue = _ref22.hasValue, controlShouldRenderValue = _ref22.selectProps.controlShouldRenderValue;
    return _objectSpread2({
      alignItems: "center",
      display: isMulti && hasValue && controlShouldRenderValue ? "flex" : "grid",
      flex: 1,
      flexWrap: "wrap",
      WebkitOverflowScrolling: "touch",
      position: "relative",
      overflow: "hidden"
    }, unstyled ? {} : {
      padding: "".concat(spacing2.baseUnit / 2, "px ").concat(spacing2.baseUnit * 2, "px")
    });
  };
  var ValueContainer = function ValueContainer2(props) {
    var children = props.children, innerProps = props.innerProps, isMulti = props.isMulti, hasValue = props.hasValue;
    return jsx("div", _extends({}, getStyleProps(props, "valueContainer", {
      "value-container": true,
      "value-container--is-multi": isMulti,
      "value-container--has-value": hasValue
    }), innerProps), children);
  };
  var indicatorsContainerCSS = function indicatorsContainerCSS2() {
    return {
      alignItems: "center",
      alignSelf: "stretch",
      display: "flex",
      flexShrink: 0
    };
  };
  var IndicatorsContainer = function IndicatorsContainer2(props) {
    var children = props.children, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "indicatorsContainer", {
      indicators: true
    }), innerProps), children);
  };
  var _templateObject;
  var _excluded$2 = ["size"], _excluded2 = ["innerProps", "isRtl", "size"];
  var _ref2$2 = {
    name: "8mmkcg",
    styles: "display:inline-block;fill:currentColor;line-height:1;stroke:currentColor;stroke-width:0"
  };
  var Svg = function Svg2(_ref3) {
    var size = _ref3.size, props = _objectWithoutProperties(_ref3, _excluded$2);
    return jsx("svg", _extends({
      height: size,
      width: size,
      viewBox: "0 0 20 20",
      "aria-hidden": "true",
      focusable: "false",
      css: _ref2$2
    }, props));
  };
  var CrossIcon = function CrossIcon2(props) {
    return jsx(Svg, _extends({
      size: 20
    }, props), jsx("path", {
      d: "M14.348 14.849c-0.469 0.469-1.229 0.469-1.697 0l-2.651-3.030-2.651 3.029c-0.469 0.469-1.229 0.469-1.697 0-0.469-0.469-0.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-0.469-0.469-0.469-1.228 0-1.697s1.228-0.469 1.697 0l2.652 3.031 2.651-3.031c0.469-0.469 1.228-0.469 1.697 0s0.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c0.469 0.469 0.469 1.229 0 1.698z"
    }));
  };
  var DownChevron = function DownChevron2(props) {
    return jsx(Svg, _extends({
      size: 20
    }, props), jsx("path", {
      d: "M4.516 7.548c0.436-0.446 1.043-0.481 1.576 0l3.908 3.747 3.908-3.747c0.533-0.481 1.141-0.446 1.574 0 0.436 0.445 0.408 1.197 0 1.615-0.406 0.418-4.695 4.502-4.695 4.502-0.217 0.223-0.502 0.335-0.787 0.335s-0.57-0.112-0.789-0.335c0 0-4.287-4.084-4.695-4.502s-0.436-1.17 0-1.615z"
    }));
  };
  var baseCSS = function baseCSS2(_ref3, unstyled) {
    var isFocused = _ref3.isFocused, _ref3$theme = _ref3.theme, baseUnit2 = _ref3$theme.spacing.baseUnit, colors2 = _ref3$theme.colors;
    return _objectSpread2({
      label: "indicatorContainer",
      display: "flex",
      transition: "color 150ms"
    }, unstyled ? {} : {
      color: isFocused ? colors2.neutral60 : colors2.neutral20,
      padding: baseUnit2 * 2,
      ":hover": {
        color: isFocused ? colors2.neutral80 : colors2.neutral40
      }
    });
  };
  var dropdownIndicatorCSS = baseCSS;
  var DropdownIndicator = function DropdownIndicator2(props) {
    var children = props.children, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "dropdownIndicator", {
      indicator: true,
      "dropdown-indicator": true
    }), innerProps), children || jsx(DownChevron, null));
  };
  var clearIndicatorCSS = baseCSS;
  var ClearIndicator = function ClearIndicator2(props) {
    var children = props.children, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "clearIndicator", {
      indicator: true,
      "clear-indicator": true
    }), innerProps), children || jsx(CrossIcon, null));
  };
  var indicatorSeparatorCSS = function indicatorSeparatorCSS2(_ref4, unstyled) {
    var isDisabled = _ref4.isDisabled, _ref4$theme = _ref4.theme, baseUnit2 = _ref4$theme.spacing.baseUnit, colors2 = _ref4$theme.colors;
    return _objectSpread2({
      label: "indicatorSeparator",
      alignSelf: "stretch",
      width: 1
    }, unstyled ? {} : {
      backgroundColor: isDisabled ? colors2.neutral10 : colors2.neutral20,
      marginBottom: baseUnit2 * 2,
      marginTop: baseUnit2 * 2
    });
  };
  var IndicatorSeparator = function IndicatorSeparator2(props) {
    var innerProps = props.innerProps;
    return jsx("span", _extends({}, innerProps, getStyleProps(props, "indicatorSeparator", {
      "indicator-separator": true
    })));
  };
  var loadingDotAnimations = keyframes(_templateObject || (_templateObject = _taggedTemplateLiteral(["\n  0%, 80%, 100% { opacity: 0; }\n  40% { opacity: 1; }\n"])));
  var loadingIndicatorCSS = function loadingIndicatorCSS2(_ref5, unstyled) {
    var isFocused = _ref5.isFocused, size = _ref5.size, _ref5$theme = _ref5.theme, colors2 = _ref5$theme.colors, baseUnit2 = _ref5$theme.spacing.baseUnit;
    return _objectSpread2({
      label: "loadingIndicator",
      display: "flex",
      transition: "color 150ms",
      alignSelf: "center",
      fontSize: size,
      lineHeight: 1,
      marginRight: size,
      textAlign: "center",
      verticalAlign: "middle"
    }, unstyled ? {} : {
      color: isFocused ? colors2.neutral60 : colors2.neutral20,
      padding: baseUnit2 * 2
    });
  };
  var LoadingDot = function LoadingDot2(_ref6) {
    var delay = _ref6.delay, offset = _ref6.offset;
    return jsx("span", {
      css: /* @__PURE__ */ css({
        animation: "".concat(loadingDotAnimations, " 1s ease-in-out ").concat(delay, "ms infinite;"),
        backgroundColor: "currentColor",
        borderRadius: "1em",
        display: "inline-block",
        marginLeft: offset ? "1em" : void 0,
        height: "1em",
        verticalAlign: "top",
        width: "1em"
      }, "", "")
    });
  };
  var LoadingIndicator = function LoadingIndicator2(_ref7) {
    var innerProps = _ref7.innerProps, isRtl = _ref7.isRtl, _ref7$size = _ref7.size, size = _ref7$size === void 0 ? 4 : _ref7$size, restProps = _objectWithoutProperties(_ref7, _excluded2);
    return jsx("div", _extends({}, getStyleProps(_objectSpread2(_objectSpread2({}, restProps), {}, {
      innerProps,
      isRtl,
      size
    }), "loadingIndicator", {
      indicator: true,
      "loading-indicator": true
    }), innerProps), jsx(LoadingDot, {
      delay: 0,
      offset: isRtl
    }), jsx(LoadingDot, {
      delay: 160,
      offset: true
    }), jsx(LoadingDot, {
      delay: 320,
      offset: !isRtl
    }));
  };
  var css$1 = function css3(_ref3, unstyled) {
    var isDisabled = _ref3.isDisabled, isFocused = _ref3.isFocused, _ref$theme = _ref3.theme, colors2 = _ref$theme.colors, borderRadius2 = _ref$theme.borderRadius, spacing2 = _ref$theme.spacing;
    return _objectSpread2({
      label: "control",
      alignItems: "center",
      cursor: "default",
      display: "flex",
      flexWrap: "wrap",
      justifyContent: "space-between",
      minHeight: spacing2.controlHeight,
      outline: "0 !important",
      position: "relative",
      transition: "all 100ms"
    }, unstyled ? {} : {
      backgroundColor: isDisabled ? colors2.neutral5 : colors2.neutral0,
      borderColor: isDisabled ? colors2.neutral10 : isFocused ? colors2.primary : colors2.neutral20,
      borderRadius: borderRadius2,
      borderStyle: "solid",
      borderWidth: 1,
      boxShadow: isFocused ? "0 0 0 1px ".concat(colors2.primary) : void 0,
      "&:hover": {
        borderColor: isFocused ? colors2.primary : colors2.neutral30
      }
    });
  };
  var Control = function Control2(props) {
    var children = props.children, isDisabled = props.isDisabled, isFocused = props.isFocused, innerRef = props.innerRef, innerProps = props.innerProps, menuIsOpen = props.menuIsOpen;
    return jsx("div", _extends({
      ref: innerRef
    }, getStyleProps(props, "control", {
      control: true,
      "control--is-disabled": isDisabled,
      "control--is-focused": isFocused,
      "control--menu-is-open": menuIsOpen
    }), innerProps, {
      "aria-disabled": isDisabled || void 0
    }), children);
  };
  var Control$1 = Control;
  var _excluded$1 = ["data"];
  var groupCSS = function groupCSS2(_ref3, unstyled) {
    var spacing2 = _ref3.theme.spacing;
    return unstyled ? {} : {
      paddingBottom: spacing2.baseUnit * 2,
      paddingTop: spacing2.baseUnit * 2
    };
  };
  var Group = function Group2(props) {
    var children = props.children, cx = props.cx, getStyles = props.getStyles, getClassNames = props.getClassNames, Heading = props.Heading, headingProps = props.headingProps, innerProps = props.innerProps, label = props.label, theme = props.theme, selectProps = props.selectProps;
    return jsx("div", _extends({}, getStyleProps(props, "group", {
      group: true
    }), innerProps), jsx(Heading, _extends({}, headingProps, {
      selectProps,
      theme,
      getStyles,
      getClassNames,
      cx
    }), label), jsx("div", null, children));
  };
  var groupHeadingCSS = function groupHeadingCSS2(_ref22, unstyled) {
    var _ref2$theme = _ref22.theme, colors2 = _ref2$theme.colors, spacing2 = _ref2$theme.spacing;
    return _objectSpread2({
      label: "group",
      cursor: "default",
      display: "block"
    }, unstyled ? {} : {
      color: colors2.neutral40,
      fontSize: "75%",
      fontWeight: 500,
      marginBottom: "0.25em",
      paddingLeft: spacing2.baseUnit * 3,
      paddingRight: spacing2.baseUnit * 3,
      textTransform: "uppercase"
    });
  };
  var GroupHeading = function GroupHeading2(props) {
    var _cleanCommonProps = cleanCommonProps(props);
    _cleanCommonProps.data;
    var innerProps = _objectWithoutProperties(_cleanCommonProps, _excluded$1);
    return jsx("div", _extends({}, getStyleProps(props, "groupHeading", {
      "group-heading": true
    }), innerProps));
  };
  var Group$1 = Group;
  var _excluded$5 = ["innerRef", "isDisabled", "isHidden", "inputClassName"];
  var inputCSS = function inputCSS2(_ref3, unstyled) {
    var isDisabled = _ref3.isDisabled, value = _ref3.value, _ref$theme = _ref3.theme, spacing2 = _ref$theme.spacing, colors2 = _ref$theme.colors;
    return _objectSpread2(_objectSpread2({
      visibility: isDisabled ? "hidden" : "visible",
      // force css to recompute when value change due to @emotion bug.
      // We can remove it whenever the bug is fixed.
      transform: value ? "translateZ(0)" : ""
    }, containerStyle), unstyled ? {} : {
      margin: spacing2.baseUnit / 2,
      paddingBottom: spacing2.baseUnit / 2,
      paddingTop: spacing2.baseUnit / 2,
      color: colors2.neutral80
    });
  };
  var spacingStyle = {
    gridArea: "1 / 2",
    font: "inherit",
    minWidth: "2px",
    border: 0,
    margin: 0,
    outline: 0,
    padding: 0
  };
  var containerStyle = {
    flex: "1 1 auto",
    display: "inline-grid",
    gridArea: "1 / 1 / 2 / 3",
    gridTemplateColumns: "0 min-content",
    "&:after": _objectSpread2({
      content: 'attr(data-value) " "',
      visibility: "hidden",
      whiteSpace: "pre"
    }, spacingStyle)
  };
  var inputStyle = function inputStyle2(isHidden) {
    return _objectSpread2({
      label: "input",
      color: "inherit",
      background: 0,
      opacity: isHidden ? 0 : 1,
      width: "100%"
    }, spacingStyle);
  };
  var Input = function Input2(props) {
    var cx = props.cx, value = props.value;
    var _cleanCommonProps = cleanCommonProps(props), innerRef = _cleanCommonProps.innerRef, isDisabled = _cleanCommonProps.isDisabled, isHidden = _cleanCommonProps.isHidden, inputClassName = _cleanCommonProps.inputClassName, innerProps = _objectWithoutProperties(_cleanCommonProps, _excluded$5);
    return jsx("div", _extends({}, getStyleProps(props, "input", {
      "input-container": true
    }), {
      "data-value": value || ""
    }), jsx("input", _extends({
      className: cx({
        input: true
      }, inputClassName),
      ref: innerRef,
      style: inputStyle(isHidden),
      disabled: isDisabled
    }, innerProps)));
  };
  var Input$1 = Input;
  var multiValueCSS = function multiValueCSS2(_ref3, unstyled) {
    var _ref$theme = _ref3.theme, spacing2 = _ref$theme.spacing, borderRadius2 = _ref$theme.borderRadius, colors2 = _ref$theme.colors;
    return _objectSpread2({
      label: "multiValue",
      display: "flex",
      minWidth: 0
    }, unstyled ? {} : {
      backgroundColor: colors2.neutral10,
      borderRadius: borderRadius2 / 2,
      margin: spacing2.baseUnit / 2
    });
  };
  var multiValueLabelCSS = function multiValueLabelCSS2(_ref22, unstyled) {
    var _ref2$theme = _ref22.theme, borderRadius2 = _ref2$theme.borderRadius, colors2 = _ref2$theme.colors, cropWithEllipsis = _ref22.cropWithEllipsis;
    return _objectSpread2({
      overflow: "hidden",
      textOverflow: cropWithEllipsis || cropWithEllipsis === void 0 ? "ellipsis" : void 0,
      whiteSpace: "nowrap"
    }, unstyled ? {} : {
      borderRadius: borderRadius2 / 2,
      color: colors2.neutral80,
      fontSize: "85%",
      padding: 3,
      paddingLeft: 6
    });
  };
  var multiValueRemoveCSS = function multiValueRemoveCSS2(_ref3, unstyled) {
    var _ref3$theme = _ref3.theme, spacing2 = _ref3$theme.spacing, borderRadius2 = _ref3$theme.borderRadius, colors2 = _ref3$theme.colors, isFocused = _ref3.isFocused;
    return _objectSpread2({
      alignItems: "center",
      display: "flex"
    }, unstyled ? {} : {
      borderRadius: borderRadius2 / 2,
      backgroundColor: isFocused ? colors2.dangerLight : void 0,
      paddingLeft: spacing2.baseUnit,
      paddingRight: spacing2.baseUnit,
      ":hover": {
        backgroundColor: colors2.dangerLight,
        color: colors2.danger
      }
    });
  };
  var MultiValueGeneric = function MultiValueGeneric2(_ref4) {
    var children = _ref4.children, innerProps = _ref4.innerProps;
    return jsx("div", innerProps, children);
  };
  var MultiValueContainer = MultiValueGeneric;
  var MultiValueLabel = MultiValueGeneric;
  function MultiValueRemove(_ref5) {
    var children = _ref5.children, innerProps = _ref5.innerProps;
    return jsx("div", _extends({
      role: "button"
    }, innerProps), children || jsx(CrossIcon, {
      size: 14
    }));
  }
  var MultiValue = function MultiValue2(props) {
    var children = props.children, components2 = props.components, data = props.data, innerProps = props.innerProps, isDisabled = props.isDisabled, removeProps3 = props.removeProps, selectProps = props.selectProps;
    var Container = components2.Container, Label = components2.Label, Remove = components2.Remove;
    return jsx(Container, {
      data,
      innerProps: _objectSpread2(_objectSpread2({}, getStyleProps(props, "multiValue", {
        "multi-value": true,
        "multi-value--is-disabled": isDisabled
      })), innerProps),
      selectProps
    }, jsx(Label, {
      data,
      innerProps: _objectSpread2({}, getStyleProps(props, "multiValueLabel", {
        "multi-value__label": true
      })),
      selectProps
    }, children), jsx(Remove, {
      data,
      innerProps: _objectSpread2(_objectSpread2({}, getStyleProps(props, "multiValueRemove", {
        "multi-value__remove": true
      })), {}, {
        "aria-label": "Remove ".concat(children || "option")
      }, removeProps3),
      selectProps
    }));
  };
  var MultiValue$1 = MultiValue;
  var optionCSS = function optionCSS2(_ref3, unstyled) {
    var isDisabled = _ref3.isDisabled, isFocused = _ref3.isFocused, isSelected = _ref3.isSelected, _ref$theme = _ref3.theme, spacing2 = _ref$theme.spacing, colors2 = _ref$theme.colors;
    return _objectSpread2({
      label: "option",
      cursor: "default",
      display: "block",
      fontSize: "inherit",
      width: "100%",
      userSelect: "none",
      WebkitTapHighlightColor: "rgba(0, 0, 0, 0)"
    }, unstyled ? {} : {
      backgroundColor: isSelected ? colors2.primary : isFocused ? colors2.primary25 : "transparent",
      color: isDisabled ? colors2.neutral20 : isSelected ? colors2.neutral0 : "inherit",
      padding: "".concat(spacing2.baseUnit * 2, "px ").concat(spacing2.baseUnit * 3, "px"),
      // provide some affordance on touch devices
      ":active": {
        backgroundColor: !isDisabled ? isSelected ? colors2.primary : colors2.primary50 : void 0
      }
    });
  };
  var Option = function Option2(props) {
    var children = props.children, isDisabled = props.isDisabled, isFocused = props.isFocused, isSelected = props.isSelected, innerRef = props.innerRef, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "option", {
      option: true,
      "option--is-disabled": isDisabled,
      "option--is-focused": isFocused,
      "option--is-selected": isSelected
    }), {
      ref: innerRef,
      "aria-disabled": isDisabled
    }, innerProps), children);
  };
  var Option$1 = Option;
  var placeholderCSS = function placeholderCSS2(_ref3, unstyled) {
    var _ref$theme = _ref3.theme, spacing2 = _ref$theme.spacing, colors2 = _ref$theme.colors;
    return _objectSpread2({
      label: "placeholder",
      gridArea: "1 / 1 / 2 / 3"
    }, unstyled ? {} : {
      color: colors2.neutral50,
      marginLeft: spacing2.baseUnit / 2,
      marginRight: spacing2.baseUnit / 2
    });
  };
  var Placeholder = function Placeholder2(props) {
    var children = props.children, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "placeholder", {
      placeholder: true
    }), innerProps), children);
  };
  var Placeholder$1 = Placeholder;
  var css2 = function css3(_ref3, unstyled) {
    var isDisabled = _ref3.isDisabled, _ref$theme = _ref3.theme, spacing2 = _ref$theme.spacing, colors2 = _ref$theme.colors;
    return _objectSpread2({
      label: "singleValue",
      gridArea: "1 / 1 / 2 / 3",
      maxWidth: "100%",
      overflow: "hidden",
      textOverflow: "ellipsis",
      whiteSpace: "nowrap"
    }, unstyled ? {} : {
      color: isDisabled ? colors2.neutral40 : colors2.neutral80,
      marginLeft: spacing2.baseUnit / 2,
      marginRight: spacing2.baseUnit / 2
    });
  };
  var SingleValue = function SingleValue2(props) {
    var children = props.children, isDisabled = props.isDisabled, innerProps = props.innerProps;
    return jsx("div", _extends({}, getStyleProps(props, "singleValue", {
      "single-value": true,
      "single-value--is-disabled": isDisabled
    }), innerProps), children);
  };
  var SingleValue$1 = SingleValue;
  var components = {
    ClearIndicator,
    Control: Control$1,
    DropdownIndicator,
    DownChevron,
    CrossIcon,
    Group: Group$1,
    GroupHeading,
    IndicatorsContainer,
    IndicatorSeparator,
    Input: Input$1,
    LoadingIndicator,
    Menu: Menu$1,
    MenuList,
    MenuPortal,
    LoadingMessage,
    NoOptionsMessage,
    MultiValue: MultiValue$1,
    MultiValueContainer,
    MultiValueLabel,
    MultiValueRemove,
    Option: Option$1,
    Placeholder: Placeholder$1,
    SelectContainer,
    SingleValue: SingleValue$1,
    ValueContainer
  };
  var defaultComponents = function defaultComponents2(props) {
    return _objectSpread2(_objectSpread2({}, components), props.components);
  };
  var safeIsNaN = Number.isNaN || function ponyfill(value) {
    return typeof value === "number" && value !== value;
  };
  function isEqual(first, second) {
    if (first === second) {
      return true;
    }
    if (safeIsNaN(first) && safeIsNaN(second)) {
      return true;
    }
    return false;
  }
  function areInputsEqual(newInputs, lastInputs) {
    if (newInputs.length !== lastInputs.length) {
      return false;
    }
    for (var i2 = 0; i2 < newInputs.length; i2++) {
      if (!isEqual(newInputs[i2], lastInputs[i2])) {
        return false;
      }
    }
    return true;
  }
  function memoizeOne(resultFn, isEqual2) {
    if (isEqual2 === void 0) {
      isEqual2 = areInputsEqual;
    }
    var cache = null;
    function memoized() {
      var newArgs = [];
      for (var _i = 0; _i < arguments.length; _i++) {
        newArgs[_i] = arguments[_i];
      }
      if (cache && cache.lastThis === this && isEqual2(newArgs, cache.lastArgs)) {
        return cache.lastResult;
      }
      var lastResult = resultFn.apply(this, newArgs);
      cache = {
        lastResult,
        lastArgs: newArgs,
        lastThis: this
      };
      return lastResult;
    }
    memoized.clear = function clear() {
      cache = null;
    };
    return memoized;
  }
  var _ref = {
    name: "7pg0cj-a11yText",
    styles: "label:a11yText;z-index:9999;border:0;clip:rect(1px, 1px, 1px, 1px);height:1px;width:1px;position:absolute;overflow:hidden;padding:0;white-space:nowrap"
  };
  var A11yText = function A11yText2(props) {
    return jsx("span", _extends({
      css: _ref
    }, props));
  };
  var A11yText$1 = A11yText;
  var defaultAriaLiveMessages = {
    guidance: function guidance(props) {
      var isSearchable = props.isSearchable, isMulti = props.isMulti, tabSelectsValue = props.tabSelectsValue, context = props.context, isInitialFocus = props.isInitialFocus;
      switch (context) {
        case "menu":
          return "Use Up and Down to choose options, press Enter to select the currently focused option, press Escape to exit the menu".concat(tabSelectsValue ? ", press Tab to select the option and exit the menu" : "", ".");
        case "input":
          return isInitialFocus ? "".concat(props["aria-label"] || "Select", " is focused ").concat(isSearchable ? ",type to refine list" : "", ", press Down to open the menu, ").concat(isMulti ? " press left to focus selected values" : "") : "";
        case "value":
          return "Use left and right to toggle between focused values, press Backspace to remove the currently focused value";
        default:
          return "";
      }
    },
    onChange: function onChange(props) {
      var action = props.action, _props$label = props.label, label = _props$label === void 0 ? "" : _props$label, labels = props.labels, isDisabled = props.isDisabled;
      switch (action) {
        case "deselect-option":
        case "pop-value":
        case "remove-value":
          return "option ".concat(label, ", deselected.");
        case "clear":
          return "All selected options have been cleared.";
        case "initial-input-focus":
          return "option".concat(labels.length > 1 ? "s" : "", " ").concat(labels.join(","), ", selected.");
        case "select-option":
          return isDisabled ? "option ".concat(label, " is disabled. Select another option.") : "option ".concat(label, ", selected.");
        default:
          return "";
      }
    },
    onFocus: function onFocus(props) {
      var context = props.context, focused = props.focused, options2 = props.options, _props$label2 = props.label, label = _props$label2 === void 0 ? "" : _props$label2, selectValue = props.selectValue, isDisabled = props.isDisabled, isSelected = props.isSelected, isAppleDevice2 = props.isAppleDevice;
      var getArrayIndex = function getArrayIndex2(arr, item) {
        return arr && arr.length ? "".concat(arr.indexOf(item) + 1, " of ").concat(arr.length) : "";
      };
      if (context === "value" && selectValue) {
        return "value ".concat(label, " focused, ").concat(getArrayIndex(selectValue, focused), ".");
      }
      if (context === "menu" && isAppleDevice2) {
        var disabled = isDisabled ? " disabled" : "";
        var status = "".concat(isSelected ? " selected" : "").concat(disabled);
        return "".concat(label).concat(status, ", ").concat(getArrayIndex(options2, focused), ".");
      }
      return "";
    },
    onFilter: function onFilter(props) {
      var inputValue = props.inputValue, resultsMessage = props.resultsMessage;
      return "".concat(resultsMessage).concat(inputValue ? " for search term " + inputValue : "", ".");
    }
  };
  var LiveRegion = function LiveRegion2(props) {
    var ariaSelection = props.ariaSelection, focusedOption = props.focusedOption, focusedValue = props.focusedValue, focusableOptions = props.focusableOptions, isFocused = props.isFocused, selectValue = props.selectValue, selectProps = props.selectProps, id = props.id, isAppleDevice2 = props.isAppleDevice;
    var ariaLiveMessages = selectProps.ariaLiveMessages, getOptionLabel4 = selectProps.getOptionLabel, inputValue = selectProps.inputValue, isMulti = selectProps.isMulti, isOptionDisabled3 = selectProps.isOptionDisabled, isSearchable = selectProps.isSearchable, menuIsOpen = selectProps.menuIsOpen, options2 = selectProps.options, screenReaderStatus2 = selectProps.screenReaderStatus, tabSelectsValue = selectProps.tabSelectsValue, isLoading = selectProps.isLoading;
    var ariaLabel = selectProps["aria-label"];
    var ariaLive = selectProps["aria-live"];
    var messages = React.useMemo(function() {
      return _objectSpread2(_objectSpread2({}, defaultAriaLiveMessages), ariaLiveMessages || {});
    }, [ariaLiveMessages]);
    var ariaSelected = React.useMemo(function() {
      var message = "";
      if (ariaSelection && messages.onChange) {
        var option = ariaSelection.option, selectedOptions = ariaSelection.options, removedValue = ariaSelection.removedValue, removedValues = ariaSelection.removedValues, value = ariaSelection.value;
        var asOption = function asOption2(val) {
          return !Array.isArray(val) ? val : null;
        };
        var selected = removedValue || option || asOption(value);
        var label = selected ? getOptionLabel4(selected) : "";
        var multiSelected = selectedOptions || removedValues || void 0;
        var labels = multiSelected ? multiSelected.map(getOptionLabel4) : [];
        var onChangeProps = _objectSpread2({
          // multiSelected items are usually items that have already been selected
          // or set by the user as a default value so we assume they are not disabled
          isDisabled: selected && isOptionDisabled3(selected, selectValue),
          label,
          labels
        }, ariaSelection);
        message = messages.onChange(onChangeProps);
      }
      return message;
    }, [ariaSelection, messages, isOptionDisabled3, selectValue, getOptionLabel4]);
    var ariaFocused = React.useMemo(function() {
      var focusMsg = "";
      var focused = focusedOption || focusedValue;
      var isSelected = !!(focusedOption && selectValue && selectValue.includes(focusedOption));
      if (focused && messages.onFocus) {
        var onFocusProps = {
          focused,
          label: getOptionLabel4(focused),
          isDisabled: isOptionDisabled3(focused, selectValue),
          isSelected,
          options: focusableOptions,
          context: focused === focusedOption ? "menu" : "value",
          selectValue,
          isAppleDevice: isAppleDevice2
        };
        focusMsg = messages.onFocus(onFocusProps);
      }
      return focusMsg;
    }, [focusedOption, focusedValue, getOptionLabel4, isOptionDisabled3, messages, focusableOptions, selectValue, isAppleDevice2]);
    var ariaResults = React.useMemo(function() {
      var resultsMsg = "";
      if (menuIsOpen && options2.length && !isLoading && messages.onFilter) {
        var resultsMessage = screenReaderStatus2({
          count: focusableOptions.length
        });
        resultsMsg = messages.onFilter({
          inputValue,
          resultsMessage
        });
      }
      return resultsMsg;
    }, [focusableOptions, inputValue, menuIsOpen, messages, options2, screenReaderStatus2, isLoading]);
    var isInitialFocus = (ariaSelection === null || ariaSelection === void 0 ? void 0 : ariaSelection.action) === "initial-input-focus";
    var ariaGuidance = React.useMemo(function() {
      var guidanceMsg = "";
      if (messages.guidance) {
        var context = focusedValue ? "value" : menuIsOpen ? "menu" : "input";
        guidanceMsg = messages.guidance({
          "aria-label": ariaLabel,
          context,
          isDisabled: focusedOption && isOptionDisabled3(focusedOption, selectValue),
          isMulti,
          isSearchable,
          tabSelectsValue,
          isInitialFocus
        });
      }
      return guidanceMsg;
    }, [ariaLabel, focusedOption, focusedValue, isMulti, isOptionDisabled3, isSearchable, menuIsOpen, messages, selectValue, tabSelectsValue, isInitialFocus]);
    var ScreenReaderText = jsx(React.Fragment, null, jsx("span", {
      id: "aria-selection"
    }, ariaSelected), jsx("span", {
      id: "aria-focused"
    }, ariaFocused), jsx("span", {
      id: "aria-results"
    }, ariaResults), jsx("span", {
      id: "aria-guidance"
    }, ariaGuidance));
    return jsx(React.Fragment, null, jsx(A11yText$1, {
      id
    }, isInitialFocus && ScreenReaderText), jsx(A11yText$1, {
      "aria-live": ariaLive,
      "aria-atomic": "false",
      "aria-relevant": "additions text",
      role: "log"
    }, isFocused && !isInitialFocus && ScreenReaderText));
  };
  var LiveRegion$1 = LiveRegion;
  var diacritics = [{
    base: "A",
    letters: "AⒶＡÀÁÂẦẤẪẨÃĀĂẰẮẴẲȦǠÄǞẢÅǺǍȀȂẠẬẶḀĄȺⱯ"
  }, {
    base: "AA",
    letters: "Ꜳ"
  }, {
    base: "AE",
    letters: "ÆǼǢ"
  }, {
    base: "AO",
    letters: "Ꜵ"
  }, {
    base: "AU",
    letters: "Ꜷ"
  }, {
    base: "AV",
    letters: "ꜸꜺ"
  }, {
    base: "AY",
    letters: "Ꜽ"
  }, {
    base: "B",
    letters: "BⒷＢḂḄḆɃƂƁ"
  }, {
    base: "C",
    letters: "CⒸＣĆĈĊČÇḈƇȻꜾ"
  }, {
    base: "D",
    letters: "DⒹＤḊĎḌḐḒḎĐƋƊƉꝹ"
  }, {
    base: "DZ",
    letters: "ǱǄ"
  }, {
    base: "Dz",
    letters: "ǲǅ"
  }, {
    base: "E",
    letters: "EⒺＥÈÉÊỀẾỄỂẼĒḔḖĔĖËẺĚȄȆẸỆȨḜĘḘḚƐƎ"
  }, {
    base: "F",
    letters: "FⒻＦḞƑꝻ"
  }, {
    base: "G",
    letters: "GⒼＧǴĜḠĞĠǦĢǤƓꞠꝽꝾ"
  }, {
    base: "H",
    letters: "HⒽＨĤḢḦȞḤḨḪĦⱧⱵꞍ"
  }, {
    base: "I",
    letters: "IⒾＩÌÍÎĨĪĬİÏḮỈǏȈȊỊĮḬƗ"
  }, {
    base: "J",
    letters: "JⒿＪĴɈ"
  }, {
    base: "K",
    letters: "KⓀＫḰǨḲĶḴƘⱩꝀꝂꝄꞢ"
  }, {
    base: "L",
    letters: "LⓁＬĿĹĽḶḸĻḼḺŁȽⱢⱠꝈꝆꞀ"
  }, {
    base: "LJ",
    letters: "Ǉ"
  }, {
    base: "Lj",
    letters: "ǈ"
  }, {
    base: "M",
    letters: "MⓂＭḾṀṂⱮƜ"
  }, {
    base: "N",
    letters: "NⓃＮǸŃÑṄŇṆŅṊṈȠƝꞐꞤ"
  }, {
    base: "NJ",
    letters: "Ǌ"
  }, {
    base: "Nj",
    letters: "ǋ"
  }, {
    base: "O",
    letters: "OⓄＯÒÓÔỒỐỖỔÕṌȬṎŌṐṒŎȮȰÖȪỎŐǑȌȎƠỜỚỠỞỢỌỘǪǬØǾƆƟꝊꝌ"
  }, {
    base: "OI",
    letters: "Ƣ"
  }, {
    base: "OO",
    letters: "Ꝏ"
  }, {
    base: "OU",
    letters: "Ȣ"
  }, {
    base: "P",
    letters: "PⓅＰṔṖƤⱣꝐꝒꝔ"
  }, {
    base: "Q",
    letters: "QⓆＱꝖꝘɊ"
  }, {
    base: "R",
    letters: "RⓇＲŔṘŘȐȒṚṜŖṞɌⱤꝚꞦꞂ"
  }, {
    base: "S",
    letters: "SⓈＳẞŚṤŜṠŠṦṢṨȘŞⱾꞨꞄ"
  }, {
    base: "T",
    letters: "TⓉＴṪŤṬȚŢṰṮŦƬƮȾꞆ"
  }, {
    base: "TZ",
    letters: "Ꜩ"
  }, {
    base: "U",
    letters: "UⓊＵÙÚÛŨṸŪṺŬÜǛǗǕǙỦŮŰǓȔȖƯỪỨỮỬỰỤṲŲṶṴɄ"
  }, {
    base: "V",
    letters: "VⓋＶṼṾƲꝞɅ"
  }, {
    base: "VY",
    letters: "Ꝡ"
  }, {
    base: "W",
    letters: "WⓌＷẀẂŴẆẄẈⱲ"
  }, {
    base: "X",
    letters: "XⓍＸẊẌ"
  }, {
    base: "Y",
    letters: "YⓎＹỲÝŶỸȲẎŸỶỴƳɎỾ"
  }, {
    base: "Z",
    letters: "ZⓏＺŹẐŻŽẒẔƵȤⱿⱫꝢ"
  }, {
    base: "a",
    letters: "aⓐａẚàáâầấẫẩãāăằắẵẳȧǡäǟảåǻǎȁȃạậặḁąⱥɐ"
  }, {
    base: "aa",
    letters: "ꜳ"
  }, {
    base: "ae",
    letters: "æǽǣ"
  }, {
    base: "ao",
    letters: "ꜵ"
  }, {
    base: "au",
    letters: "ꜷ"
  }, {
    base: "av",
    letters: "ꜹꜻ"
  }, {
    base: "ay",
    letters: "ꜽ"
  }, {
    base: "b",
    letters: "bⓑｂḃḅḇƀƃɓ"
  }, {
    base: "c",
    letters: "cⓒｃćĉċčçḉƈȼꜿↄ"
  }, {
    base: "d",
    letters: "dⓓｄḋďḍḑḓḏđƌɖɗꝺ"
  }, {
    base: "dz",
    letters: "ǳǆ"
  }, {
    base: "e",
    letters: "eⓔｅèéêềếễểẽēḕḗĕėëẻěȅȇẹệȩḝęḙḛɇɛǝ"
  }, {
    base: "f",
    letters: "fⓕｆḟƒꝼ"
  }, {
    base: "g",
    letters: "gⓖｇǵĝḡğġǧģǥɠꞡᵹꝿ"
  }, {
    base: "h",
    letters: "hⓗｈĥḣḧȟḥḩḫẖħⱨⱶɥ"
  }, {
    base: "hv",
    letters: "ƕ"
  }, {
    base: "i",
    letters: "iⓘｉìíîĩīĭïḯỉǐȉȋịįḭɨı"
  }, {
    base: "j",
    letters: "jⓙｊĵǰɉ"
  }, {
    base: "k",
    letters: "kⓚｋḱǩḳķḵƙⱪꝁꝃꝅꞣ"
  }, {
    base: "l",
    letters: "lⓛｌŀĺľḷḹļḽḻſłƚɫⱡꝉꞁꝇ"
  }, {
    base: "lj",
    letters: "ǉ"
  }, {
    base: "m",
    letters: "mⓜｍḿṁṃɱɯ"
  }, {
    base: "n",
    letters: "nⓝｎǹńñṅňṇņṋṉƞɲŉꞑꞥ"
  }, {
    base: "nj",
    letters: "ǌ"
  }, {
    base: "o",
    letters: "oⓞｏòóôồốỗổõṍȭṏōṑṓŏȯȱöȫỏőǒȍȏơờớỡởợọộǫǭøǿɔꝋꝍɵ"
  }, {
    base: "oi",
    letters: "ƣ"
  }, {
    base: "ou",
    letters: "ȣ"
  }, {
    base: "oo",
    letters: "ꝏ"
  }, {
    base: "p",
    letters: "pⓟｐṕṗƥᵽꝑꝓꝕ"
  }, {
    base: "q",
    letters: "qⓠｑɋꝗꝙ"
  }, {
    base: "r",
    letters: "rⓡｒŕṙřȑȓṛṝŗṟɍɽꝛꞧꞃ"
  }, {
    base: "s",
    letters: "sⓢｓßśṥŝṡšṧṣṩșşȿꞩꞅẛ"
  }, {
    base: "t",
    letters: "tⓣｔṫẗťṭțţṱṯŧƭʈⱦꞇ"
  }, {
    base: "tz",
    letters: "ꜩ"
  }, {
    base: "u",
    letters: "uⓤｕùúûũṹūṻŭüǜǘǖǚủůűǔȕȗưừứữửựụṳųṷṵʉ"
  }, {
    base: "v",
    letters: "vⓥｖṽṿʋꝟʌ"
  }, {
    base: "vy",
    letters: "ꝡ"
  }, {
    base: "w",
    letters: "wⓦｗẁẃŵẇẅẘẉⱳ"
  }, {
    base: "x",
    letters: "xⓧｘẋẍ"
  }, {
    base: "y",
    letters: "yⓨｙỳýŷỹȳẏÿỷẙỵƴɏỿ"
  }, {
    base: "z",
    letters: "zⓩｚźẑżžẓẕƶȥɀⱬꝣ"
  }];
  var anyDiacritic = new RegExp("[" + diacritics.map(function(d2) {
    return d2.letters;
  }).join("") + "]", "g");
  var diacriticToBase = {};
  for (var i = 0; i < diacritics.length; i++) {
    var diacritic = diacritics[i];
    for (var j = 0; j < diacritic.letters.length; j++) {
      diacriticToBase[diacritic.letters[j]] = diacritic.base;
    }
  }
  var stripDiacritics = function stripDiacritics2(str) {
    return str.replace(anyDiacritic, function(match2) {
      return diacriticToBase[match2];
    });
  };
  var memoizedStripDiacriticsForInput = memoizeOne(stripDiacritics);
  var trimString = function trimString2(str) {
    return str.replace(/^\s+|\s+$/g, "");
  };
  var defaultStringify = function defaultStringify2(option) {
    return "".concat(option.label, " ").concat(option.value);
  };
  var createFilter = function createFilter2(config) {
    return function(option, rawInput) {
      if (option.data.__isNew__) return true;
      var _ignoreCase$ignoreAcc = _objectSpread2({
        ignoreCase: true,
        ignoreAccents: true,
        stringify: defaultStringify,
        trim: true,
        matchFrom: "any"
      }, config), ignoreCase = _ignoreCase$ignoreAcc.ignoreCase, ignoreAccents = _ignoreCase$ignoreAcc.ignoreAccents, stringify2 = _ignoreCase$ignoreAcc.stringify, trim2 = _ignoreCase$ignoreAcc.trim, matchFrom = _ignoreCase$ignoreAcc.matchFrom;
      var input = trim2 ? trimString(rawInput) : rawInput;
      var candidate = trim2 ? trimString(stringify2(option)) : stringify2(option);
      if (ignoreCase) {
        input = input.toLowerCase();
        candidate = candidate.toLowerCase();
      }
      if (ignoreAccents) {
        input = memoizedStripDiacriticsForInput(input);
        candidate = stripDiacritics(candidate);
      }
      return matchFrom === "start" ? candidate.substr(0, input.length) === input : candidate.indexOf(input) > -1;
    };
  };
  var _excluded = ["innerRef"];
  function DummyInput(_ref3) {
    var innerRef = _ref3.innerRef, props = _objectWithoutProperties(_ref3, _excluded);
    var filteredProps = removeProps(props, "onExited", "in", "enter", "exit", "appear");
    return jsx("input", _extends({
      ref: innerRef
    }, filteredProps, {
      css: /* @__PURE__ */ css({
        label: "dummyInput",
        // get rid of any default styles
        background: 0,
        border: 0,
        // important! this hides the flashing cursor
        caretColor: "transparent",
        fontSize: "inherit",
        gridArea: "1 / 1 / 2 / 3",
        outline: 0,
        padding: 0,
        // important! without `width` browsers won't allow focus
        width: 1,
        // remove cursor on desktop
        color: "transparent",
        // remove cursor on mobile whilst maintaining "scroll into view" behaviour
        left: -100,
        opacity: 0,
        position: "relative",
        transform: "scale(.01)"
      }, "", "")
    }));
  }
  var cancelScroll = function cancelScroll2(event) {
    if (event.cancelable) event.preventDefault();
    event.stopPropagation();
  };
  function useScrollCapture(_ref3) {
    var isEnabled = _ref3.isEnabled, onBottomArrive = _ref3.onBottomArrive, onBottomLeave = _ref3.onBottomLeave, onTopArrive = _ref3.onTopArrive, onTopLeave = _ref3.onTopLeave;
    var isBottom = React.useRef(false);
    var isTop = React.useRef(false);
    var touchStart = React.useRef(0);
    var scrollTarget = React.useRef(null);
    var handleEventDelta = React.useCallback(function(event, delta) {
      if (scrollTarget.current === null) return;
      var _scrollTarget$current = scrollTarget.current, scrollTop = _scrollTarget$current.scrollTop, scrollHeight = _scrollTarget$current.scrollHeight, clientHeight = _scrollTarget$current.clientHeight;
      var target = scrollTarget.current;
      var isDeltaPositive = delta > 0;
      var availableScroll = scrollHeight - clientHeight - scrollTop;
      var shouldCancelScroll = false;
      if (availableScroll > delta && isBottom.current) {
        if (onBottomLeave) onBottomLeave(event);
        isBottom.current = false;
      }
      if (isDeltaPositive && isTop.current) {
        if (onTopLeave) onTopLeave(event);
        isTop.current = false;
      }
      if (isDeltaPositive && delta > availableScroll) {
        if (onBottomArrive && !isBottom.current) {
          onBottomArrive(event);
        }
        target.scrollTop = scrollHeight;
        shouldCancelScroll = true;
        isBottom.current = true;
      } else if (!isDeltaPositive && -delta > scrollTop) {
        if (onTopArrive && !isTop.current) {
          onTopArrive(event);
        }
        target.scrollTop = 0;
        shouldCancelScroll = true;
        isTop.current = true;
      }
      if (shouldCancelScroll) {
        cancelScroll(event);
      }
    }, [onBottomArrive, onBottomLeave, onTopArrive, onTopLeave]);
    var onWheel = React.useCallback(function(event) {
      handleEventDelta(event, event.deltaY);
    }, [handleEventDelta]);
    var onTouchStart = React.useCallback(function(event) {
      touchStart.current = event.changedTouches[0].clientY;
    }, []);
    var onTouchMove = React.useCallback(function(event) {
      var deltaY = touchStart.current - event.changedTouches[0].clientY;
      handleEventDelta(event, deltaY);
    }, [handleEventDelta]);
    var startListening = React.useCallback(function(el) {
      if (!el) return;
      var notPassive = supportsPassiveEvents ? {
        passive: false
      } : false;
      el.addEventListener("wheel", onWheel, notPassive);
      el.addEventListener("touchstart", onTouchStart, notPassive);
      el.addEventListener("touchmove", onTouchMove, notPassive);
    }, [onTouchMove, onTouchStart, onWheel]);
    var stopListening = React.useCallback(function(el) {
      if (!el) return;
      el.removeEventListener("wheel", onWheel, false);
      el.removeEventListener("touchstart", onTouchStart, false);
      el.removeEventListener("touchmove", onTouchMove, false);
    }, [onTouchMove, onTouchStart, onWheel]);
    React.useEffect(function() {
      if (!isEnabled) return;
      var element = scrollTarget.current;
      startListening(element);
      return function() {
        stopListening(element);
      };
    }, [isEnabled, startListening, stopListening]);
    return function(element) {
      scrollTarget.current = element;
    };
  }
  var STYLE_KEYS = ["boxSizing", "height", "overflow", "paddingRight", "position"];
  var LOCK_STYLES = {
    boxSizing: "border-box",
    // account for possible declaration `width: 100%;` on body
    overflow: "hidden",
    position: "relative",
    height: "100%"
  };
  function preventTouchMove(e2) {
    if (e2.cancelable) e2.preventDefault();
  }
  function allowTouchMove(e2) {
    e2.stopPropagation();
  }
  function preventInertiaScroll() {
    var top = this.scrollTop;
    var totalScroll = this.scrollHeight;
    var currentScroll = top + this.offsetHeight;
    if (top === 0) {
      this.scrollTop = 1;
    } else if (currentScroll === totalScroll) {
      this.scrollTop = top - 1;
    }
  }
  function isTouchDevice() {
    return "ontouchstart" in window || navigator.maxTouchPoints;
  }
  var canUseDOM = !!(typeof window !== "undefined" && window.document && window.document.createElement);
  var activeScrollLocks = 0;
  var listenerOptions = {
    capture: false,
    passive: false
  };
  function useScrollLock(_ref3) {
    var isEnabled = _ref3.isEnabled, _ref$accountForScroll = _ref3.accountForScrollbars, accountForScrollbars = _ref$accountForScroll === void 0 ? true : _ref$accountForScroll;
    var originalStyles = React.useRef({});
    var scrollTarget = React.useRef(null);
    var addScrollLock = React.useCallback(function(touchScrollTarget) {
      if (!canUseDOM) return;
      var target = document.body;
      var targetStyle = target && target.style;
      if (accountForScrollbars) {
        STYLE_KEYS.forEach(function(key) {
          var val = targetStyle && targetStyle[key];
          originalStyles.current[key] = val;
        });
      }
      if (accountForScrollbars && activeScrollLocks < 1) {
        var currentPadding = parseInt(originalStyles.current.paddingRight, 10) || 0;
        var clientWidth = document.body ? document.body.clientWidth : 0;
        var adjustedPadding = window.innerWidth - clientWidth + currentPadding || 0;
        Object.keys(LOCK_STYLES).forEach(function(key) {
          var val = LOCK_STYLES[key];
          if (targetStyle) {
            targetStyle[key] = val;
          }
        });
        if (targetStyle) {
          targetStyle.paddingRight = "".concat(adjustedPadding, "px");
        }
      }
      if (target && isTouchDevice()) {
        target.addEventListener("touchmove", preventTouchMove, listenerOptions);
        if (touchScrollTarget) {
          touchScrollTarget.addEventListener("touchstart", preventInertiaScroll, listenerOptions);
          touchScrollTarget.addEventListener("touchmove", allowTouchMove, listenerOptions);
        }
      }
      activeScrollLocks += 1;
    }, [accountForScrollbars]);
    var removeScrollLock = React.useCallback(function(touchScrollTarget) {
      if (!canUseDOM) return;
      var target = document.body;
      var targetStyle = target && target.style;
      activeScrollLocks = Math.max(activeScrollLocks - 1, 0);
      if (accountForScrollbars && activeScrollLocks < 1) {
        STYLE_KEYS.forEach(function(key) {
          var val = originalStyles.current[key];
          if (targetStyle) {
            targetStyle[key] = val;
          }
        });
      }
      if (target && isTouchDevice()) {
        target.removeEventListener("touchmove", preventTouchMove, listenerOptions);
        if (touchScrollTarget) {
          touchScrollTarget.removeEventListener("touchstart", preventInertiaScroll, listenerOptions);
          touchScrollTarget.removeEventListener("touchmove", allowTouchMove, listenerOptions);
        }
      }
    }, [accountForScrollbars]);
    React.useEffect(function() {
      if (!isEnabled) return;
      var element = scrollTarget.current;
      addScrollLock(element);
      return function() {
        removeScrollLock(element);
      };
    }, [isEnabled, addScrollLock, removeScrollLock]);
    return function(element) {
      scrollTarget.current = element;
    };
  }
  var blurSelectInput = function blurSelectInput2(event) {
    var element = event.target;
    return element.ownerDocument.activeElement && element.ownerDocument.activeElement.blur();
  };
  var _ref2$1 = {
    name: "1kfdb0e",
    styles: "position:fixed;left:0;bottom:0;right:0;top:0"
  };
  function ScrollManager(_ref3) {
    var children = _ref3.children, lockEnabled = _ref3.lockEnabled, _ref$captureEnabled = _ref3.captureEnabled, captureEnabled = _ref$captureEnabled === void 0 ? true : _ref$captureEnabled, onBottomArrive = _ref3.onBottomArrive, onBottomLeave = _ref3.onBottomLeave, onTopArrive = _ref3.onTopArrive, onTopLeave = _ref3.onTopLeave;
    var setScrollCaptureTarget = useScrollCapture({
      isEnabled: captureEnabled,
      onBottomArrive,
      onBottomLeave,
      onTopArrive,
      onTopLeave
    });
    var setScrollLockTarget = useScrollLock({
      isEnabled: lockEnabled
    });
    var targetRef = function targetRef2(element) {
      setScrollCaptureTarget(element);
      setScrollLockTarget(element);
    };
    return jsx(React.Fragment, null, lockEnabled && jsx("div", {
      onClick: blurSelectInput,
      css: _ref2$1
    }), children(targetRef));
  }
  var _ref2 = {
    name: "1a0ro4n-requiredInput",
    styles: "label:requiredInput;opacity:0;pointer-events:none;position:absolute;bottom:0;left:0;right:0;width:100%"
  };
  var RequiredInput = function RequiredInput2(_ref3) {
    var name = _ref3.name, onFocus2 = _ref3.onFocus;
    return jsx("input", {
      required: true,
      name,
      tabIndex: -1,
      "aria-hidden": "true",
      onFocus: onFocus2,
      css: _ref2,
      value: "",
      onChange: function onChange2() {
      }
    });
  };
  var RequiredInput$1 = RequiredInput;
  function testPlatform(re) {
    var _window$navigator$use;
    return typeof window !== "undefined" && window.navigator != null ? re.test(((_window$navigator$use = window.navigator["userAgentData"]) === null || _window$navigator$use === void 0 ? void 0 : _window$navigator$use.platform) || window.navigator.platform) : false;
  }
  function isIPhone() {
    return testPlatform(/^iPhone/i);
  }
  function isMac() {
    return testPlatform(/^Mac/i);
  }
  function isIPad() {
    return testPlatform(/^iPad/i) || // iPadOS 13 lies and says it's a Mac, but we can distinguish by detecting touch support.
    isMac() && navigator.maxTouchPoints > 1;
  }
  function isIOS() {
    return isIPhone() || isIPad();
  }
  function isAppleDevice() {
    return isMac() || isIOS();
  }
  var formatGroupLabel = function formatGroupLabel2(group) {
    return group.label;
  };
  var getOptionLabel$1 = function getOptionLabel(option) {
    return option.label;
  };
  var getOptionValue$1 = function getOptionValue(option) {
    return option.value;
  };
  var isOptionDisabled = function isOptionDisabled2(option) {
    return !!option.isDisabled;
  };
  var defaultStyles = {
    clearIndicator: clearIndicatorCSS,
    container: containerCSS,
    control: css$1,
    dropdownIndicator: dropdownIndicatorCSS,
    group: groupCSS,
    groupHeading: groupHeadingCSS,
    indicatorsContainer: indicatorsContainerCSS,
    indicatorSeparator: indicatorSeparatorCSS,
    input: inputCSS,
    loadingIndicator: loadingIndicatorCSS,
    loadingMessage: loadingMessageCSS,
    menu: menuCSS,
    menuList: menuListCSS,
    menuPortal: menuPortalCSS,
    multiValue: multiValueCSS,
    multiValueLabel: multiValueLabelCSS,
    multiValueRemove: multiValueRemoveCSS,
    noOptionsMessage: noOptionsMessageCSS,
    option: optionCSS,
    placeholder: placeholderCSS,
    singleValue: css2,
    valueContainer: valueContainerCSS
  };
  var colors = {
    primary: "#2684FF",
    primary75: "#4C9AFF",
    primary50: "#B2D4FF",
    primary25: "#DEEBFF",
    danger: "#DE350B",
    dangerLight: "#FFBDAD",
    neutral0: "hsl(0, 0%, 100%)",
    neutral5: "hsl(0, 0%, 95%)",
    neutral10: "hsl(0, 0%, 90%)",
    neutral20: "hsl(0, 0%, 80%)",
    neutral30: "hsl(0, 0%, 70%)",
    neutral40: "hsl(0, 0%, 60%)",
    neutral50: "hsl(0, 0%, 50%)",
    neutral60: "hsl(0, 0%, 40%)",
    neutral70: "hsl(0, 0%, 30%)",
    neutral80: "hsl(0, 0%, 20%)",
    neutral90: "hsl(0, 0%, 10%)"
  };
  var borderRadius = 4;
  var baseUnit = 4;
  var controlHeight = 38;
  var menuGutter = baseUnit * 2;
  var spacing = {
    baseUnit,
    controlHeight,
    menuGutter
  };
  var defaultTheme = {
    borderRadius,
    colors,
    spacing
  };
  var defaultProps = {
    "aria-live": "polite",
    backspaceRemovesValue: true,
    blurInputOnSelect: isTouchCapable(),
    captureMenuScroll: !isTouchCapable(),
    classNames: {},
    closeMenuOnSelect: true,
    closeMenuOnScroll: false,
    components: {},
    controlShouldRenderValue: true,
    escapeClearsValue: false,
    filterOption: createFilter(),
    formatGroupLabel,
    getOptionLabel: getOptionLabel$1,
    getOptionValue: getOptionValue$1,
    isDisabled: false,
    isLoading: false,
    isMulti: false,
    isRtl: false,
    isSearchable: true,
    isOptionDisabled,
    loadingMessage: function loadingMessage() {
      return "Loading...";
    },
    maxMenuHeight: 300,
    minMenuHeight: 140,
    menuIsOpen: false,
    menuPlacement: "bottom",
    menuPosition: "absolute",
    menuShouldBlockScroll: false,
    menuShouldScrollIntoView: !isMobileDevice(),
    noOptionsMessage: function noOptionsMessage() {
      return "No options";
    },
    openMenuOnFocus: false,
    openMenuOnClick: true,
    options: [],
    pageSize: 5,
    placeholder: "Select...",
    screenReaderStatus: function screenReaderStatus(_ref3) {
      var count = _ref3.count;
      return "".concat(count, " result").concat(count !== 1 ? "s" : "", " available");
    },
    styles: {},
    tabIndex: 0,
    tabSelectsValue: true,
    unstyled: false
  };
  function toCategorizedOption(props, option, selectValue, index2) {
    var isDisabled = _isOptionDisabled(props, option, selectValue);
    var isSelected = _isOptionSelected(props, option, selectValue);
    var label = getOptionLabel2(props, option);
    var value = getOptionValue2(props, option);
    return {
      type: "option",
      data: option,
      isDisabled,
      isSelected,
      label,
      value,
      index: index2
    };
  }
  function buildCategorizedOptions(props, selectValue) {
    return props.options.map(function(groupOrOption, groupOrOptionIndex) {
      if ("options" in groupOrOption) {
        var categorizedOptions = groupOrOption.options.map(function(option, optionIndex) {
          return toCategorizedOption(props, option, selectValue, optionIndex);
        }).filter(function(categorizedOption2) {
          return isFocusable(props, categorizedOption2);
        });
        return categorizedOptions.length > 0 ? {
          type: "group",
          data: groupOrOption,
          options: categorizedOptions,
          index: groupOrOptionIndex
        } : void 0;
      }
      var categorizedOption = toCategorizedOption(props, groupOrOption, selectValue, groupOrOptionIndex);
      return isFocusable(props, categorizedOption) ? categorizedOption : void 0;
    }).filter(notNullish);
  }
  function buildFocusableOptionsFromCategorizedOptions(categorizedOptions) {
    return categorizedOptions.reduce(function(optionsAccumulator, categorizedOption) {
      if (categorizedOption.type === "group") {
        optionsAccumulator.push.apply(optionsAccumulator, _toConsumableArray(categorizedOption.options.map(function(option) {
          return option.data;
        })));
      } else {
        optionsAccumulator.push(categorizedOption.data);
      }
      return optionsAccumulator;
    }, []);
  }
  function buildFocusableOptionsWithIds(categorizedOptions, optionId) {
    return categorizedOptions.reduce(function(optionsAccumulator, categorizedOption) {
      if (categorizedOption.type === "group") {
        optionsAccumulator.push.apply(optionsAccumulator, _toConsumableArray(categorizedOption.options.map(function(option) {
          return {
            data: option.data,
            id: "".concat(optionId, "-").concat(categorizedOption.index, "-").concat(option.index)
          };
        })));
      } else {
        optionsAccumulator.push({
          data: categorizedOption.data,
          id: "".concat(optionId, "-").concat(categorizedOption.index)
        });
      }
      return optionsAccumulator;
    }, []);
  }
  function buildFocusableOptions(props, selectValue) {
    return buildFocusableOptionsFromCategorizedOptions(buildCategorizedOptions(props, selectValue));
  }
  function isFocusable(props, categorizedOption) {
    var _props$inputValue = props.inputValue, inputValue = _props$inputValue === void 0 ? "" : _props$inputValue;
    var data = categorizedOption.data, isSelected = categorizedOption.isSelected, label = categorizedOption.label, value = categorizedOption.value;
    return (!shouldHideSelectedOptions(props) || !isSelected) && _filterOption(props, {
      label,
      value,
      data
    }, inputValue);
  }
  function getNextFocusedValue(state, nextSelectValue) {
    var focusedValue = state.focusedValue, lastSelectValue = state.selectValue;
    var lastFocusedIndex = lastSelectValue.indexOf(focusedValue);
    if (lastFocusedIndex > -1) {
      var nextFocusedIndex = nextSelectValue.indexOf(focusedValue);
      if (nextFocusedIndex > -1) {
        return focusedValue;
      } else if (lastFocusedIndex < nextSelectValue.length) {
        return nextSelectValue[lastFocusedIndex];
      }
    }
    return null;
  }
  function getNextFocusedOption(state, options2) {
    var lastFocusedOption = state.focusedOption;
    return lastFocusedOption && options2.indexOf(lastFocusedOption) > -1 ? lastFocusedOption : options2[0];
  }
  var getFocusedOptionId = function getFocusedOptionId2(focusableOptionsWithIds, focusedOption) {
    var _focusableOptionsWith;
    var focusedOptionId = (_focusableOptionsWith = focusableOptionsWithIds.find(function(option) {
      return option.data === focusedOption;
    })) === null || _focusableOptionsWith === void 0 ? void 0 : _focusableOptionsWith.id;
    return focusedOptionId || null;
  };
  var getOptionLabel2 = function getOptionLabel3(props, data) {
    return props.getOptionLabel(data);
  };
  var getOptionValue2 = function getOptionValue3(props, data) {
    return props.getOptionValue(data);
  };
  function _isOptionDisabled(props, option, selectValue) {
    return typeof props.isOptionDisabled === "function" ? props.isOptionDisabled(option, selectValue) : false;
  }
  function _isOptionSelected(props, option, selectValue) {
    if (selectValue.indexOf(option) > -1) return true;
    if (typeof props.isOptionSelected === "function") {
      return props.isOptionSelected(option, selectValue);
    }
    var candidate = getOptionValue2(props, option);
    return selectValue.some(function(i2) {
      return getOptionValue2(props, i2) === candidate;
    });
  }
  function _filterOption(props, option, inputValue) {
    return props.filterOption ? props.filterOption(option, inputValue) : true;
  }
  var shouldHideSelectedOptions = function shouldHideSelectedOptions2(props) {
    var hideSelectedOptions = props.hideSelectedOptions, isMulti = props.isMulti;
    if (hideSelectedOptions === void 0) return isMulti;
    return hideSelectedOptions;
  };
  var instanceId = 1;
  var Select$1 = /* @__PURE__ */ function(_Component) {
    _inherits(Select2, _Component);
    var _super = _createSuper(Select2);
    function Select2(_props) {
      var _this;
      _classCallCheck(this, Select2);
      _this = _super.call(this, _props);
      _this.state = {
        ariaSelection: null,
        focusedOption: null,
        focusedOptionId: null,
        focusableOptionsWithIds: [],
        focusedValue: null,
        inputIsHidden: false,
        isFocused: false,
        selectValue: [],
        clearFocusValueOnUpdate: false,
        prevWasFocused: false,
        inputIsHiddenAfterUpdate: void 0,
        prevProps: void 0,
        instancePrefix: "",
        isAppleDevice: false
      };
      _this.blockOptionHover = false;
      _this.isComposing = false;
      _this.commonProps = void 0;
      _this.initialTouchX = 0;
      _this.initialTouchY = 0;
      _this.openAfterFocus = false;
      _this.scrollToFocusedOptionOnUpdate = false;
      _this.userIsDragging = void 0;
      _this.controlRef = null;
      _this.getControlRef = function(ref) {
        _this.controlRef = ref;
      };
      _this.focusedOptionRef = null;
      _this.getFocusedOptionRef = function(ref) {
        _this.focusedOptionRef = ref;
      };
      _this.menuListRef = null;
      _this.getMenuListRef = function(ref) {
        _this.menuListRef = ref;
      };
      _this.inputRef = null;
      _this.getInputRef = function(ref) {
        _this.inputRef = ref;
      };
      _this.focus = _this.focusInput;
      _this.blur = _this.blurInput;
      _this.onChange = function(newValue, actionMeta) {
        var _this$props = _this.props, onChange2 = _this$props.onChange, name = _this$props.name;
        actionMeta.name = name;
        _this.ariaOnChange(newValue, actionMeta);
        onChange2(newValue, actionMeta);
      };
      _this.setValue = function(newValue, action, option) {
        var _this$props2 = _this.props, closeMenuOnSelect = _this$props2.closeMenuOnSelect, isMulti = _this$props2.isMulti, inputValue = _this$props2.inputValue;
        _this.onInputChange("", {
          action: "set-value",
          prevInputValue: inputValue
        });
        if (closeMenuOnSelect) {
          _this.setState({
            inputIsHiddenAfterUpdate: !isMulti
          });
          _this.onMenuClose();
        }
        _this.setState({
          clearFocusValueOnUpdate: true
        });
        _this.onChange(newValue, {
          action,
          option
        });
      };
      _this.selectOption = function(newValue) {
        var _this$props3 = _this.props, blurInputOnSelect = _this$props3.blurInputOnSelect, isMulti = _this$props3.isMulti, name = _this$props3.name;
        var selectValue = _this.state.selectValue;
        var deselected = isMulti && _this.isOptionSelected(newValue, selectValue);
        var isDisabled = _this.isOptionDisabled(newValue, selectValue);
        if (deselected) {
          var candidate = _this.getOptionValue(newValue);
          _this.setValue(multiValueAsValue(selectValue.filter(function(i2) {
            return _this.getOptionValue(i2) !== candidate;
          })), "deselect-option", newValue);
        } else if (!isDisabled) {
          if (isMulti) {
            _this.setValue(multiValueAsValue([].concat(_toConsumableArray(selectValue), [newValue])), "select-option", newValue);
          } else {
            _this.setValue(singleValueAsValue(newValue), "select-option");
          }
        } else {
          _this.ariaOnChange(singleValueAsValue(newValue), {
            action: "select-option",
            option: newValue,
            name
          });
          return;
        }
        if (blurInputOnSelect) {
          _this.blurInput();
        }
      };
      _this.removeValue = function(removedValue) {
        var isMulti = _this.props.isMulti;
        var selectValue = _this.state.selectValue;
        var candidate = _this.getOptionValue(removedValue);
        var newValueArray = selectValue.filter(function(i2) {
          return _this.getOptionValue(i2) !== candidate;
        });
        var newValue = valueTernary(isMulti, newValueArray, newValueArray[0] || null);
        _this.onChange(newValue, {
          action: "remove-value",
          removedValue
        });
        _this.focusInput();
      };
      _this.clearValue = function() {
        var selectValue = _this.state.selectValue;
        _this.onChange(valueTernary(_this.props.isMulti, [], null), {
          action: "clear",
          removedValues: selectValue
        });
      };
      _this.popValue = function() {
        var isMulti = _this.props.isMulti;
        var selectValue = _this.state.selectValue;
        var lastSelectedValue = selectValue[selectValue.length - 1];
        var newValueArray = selectValue.slice(0, selectValue.length - 1);
        var newValue = valueTernary(isMulti, newValueArray, newValueArray[0] || null);
        if (lastSelectedValue) {
          _this.onChange(newValue, {
            action: "pop-value",
            removedValue: lastSelectedValue
          });
        }
      };
      _this.getFocusedOptionId = function(focusedOption) {
        return getFocusedOptionId(_this.state.focusableOptionsWithIds, focusedOption);
      };
      _this.getFocusableOptionsWithIds = function() {
        return buildFocusableOptionsWithIds(buildCategorizedOptions(_this.props, _this.state.selectValue), _this.getElementId("option"));
      };
      _this.getValue = function() {
        return _this.state.selectValue;
      };
      _this.cx = function() {
        for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
          args[_key] = arguments[_key];
        }
        return classNames.apply(void 0, [_this.props.classNamePrefix].concat(args));
      };
      _this.getOptionLabel = function(data) {
        return getOptionLabel2(_this.props, data);
      };
      _this.getOptionValue = function(data) {
        return getOptionValue2(_this.props, data);
      };
      _this.getStyles = function(key, props) {
        var unstyled = _this.props.unstyled;
        var base = defaultStyles[key](props, unstyled);
        base.boxSizing = "border-box";
        var custom = _this.props.styles[key];
        return custom ? custom(base, props) : base;
      };
      _this.getClassNames = function(key, props) {
        var _this$props$className, _this$props$className2;
        return (_this$props$className = (_this$props$className2 = _this.props.classNames)[key]) === null || _this$props$className === void 0 ? void 0 : _this$props$className.call(_this$props$className2, props);
      };
      _this.getElementId = function(element) {
        return "".concat(_this.state.instancePrefix, "-").concat(element);
      };
      _this.getComponents = function() {
        return defaultComponents(_this.props);
      };
      _this.buildCategorizedOptions = function() {
        return buildCategorizedOptions(_this.props, _this.state.selectValue);
      };
      _this.getCategorizedOptions = function() {
        return _this.props.menuIsOpen ? _this.buildCategorizedOptions() : [];
      };
      _this.buildFocusableOptions = function() {
        return buildFocusableOptionsFromCategorizedOptions(_this.buildCategorizedOptions());
      };
      _this.getFocusableOptions = function() {
        return _this.props.menuIsOpen ? _this.buildFocusableOptions() : [];
      };
      _this.ariaOnChange = function(value, actionMeta) {
        _this.setState({
          ariaSelection: _objectSpread2({
            value
          }, actionMeta)
        });
      };
      _this.onMenuMouseDown = function(event) {
        if (event.button !== 0) {
          return;
        }
        event.stopPropagation();
        event.preventDefault();
        _this.focusInput();
      };
      _this.onMenuMouseMove = function(event) {
        _this.blockOptionHover = false;
      };
      _this.onControlMouseDown = function(event) {
        if (event.defaultPrevented) {
          return;
        }
        var openMenuOnClick = _this.props.openMenuOnClick;
        if (!_this.state.isFocused) {
          if (openMenuOnClick) {
            _this.openAfterFocus = true;
          }
          _this.focusInput();
        } else if (!_this.props.menuIsOpen) {
          if (openMenuOnClick) {
            _this.openMenu("first");
          }
        } else {
          if (event.target.tagName !== "INPUT" && event.target.tagName !== "TEXTAREA") {
            _this.onMenuClose();
          }
        }
        if (event.target.tagName !== "INPUT" && event.target.tagName !== "TEXTAREA") {
          event.preventDefault();
        }
      };
      _this.onDropdownIndicatorMouseDown = function(event) {
        if (event && event.type === "mousedown" && event.button !== 0) {
          return;
        }
        if (_this.props.isDisabled) return;
        var _this$props4 = _this.props, isMulti = _this$props4.isMulti, menuIsOpen = _this$props4.menuIsOpen;
        _this.focusInput();
        if (menuIsOpen) {
          _this.setState({
            inputIsHiddenAfterUpdate: !isMulti
          });
          _this.onMenuClose();
        } else {
          _this.openMenu("first");
        }
        event.preventDefault();
      };
      _this.onClearIndicatorMouseDown = function(event) {
        if (event && event.type === "mousedown" && event.button !== 0) {
          return;
        }
        _this.clearValue();
        event.preventDefault();
        _this.openAfterFocus = false;
        if (event.type === "touchend") {
          _this.focusInput();
        } else {
          setTimeout(function() {
            return _this.focusInput();
          });
        }
      };
      _this.onScroll = function(event) {
        if (typeof _this.props.closeMenuOnScroll === "boolean") {
          if (event.target instanceof HTMLElement && isDocumentElement(event.target)) {
            _this.props.onMenuClose();
          }
        } else if (typeof _this.props.closeMenuOnScroll === "function") {
          if (_this.props.closeMenuOnScroll(event)) {
            _this.props.onMenuClose();
          }
        }
      };
      _this.onCompositionStart = function() {
        _this.isComposing = true;
      };
      _this.onCompositionEnd = function() {
        _this.isComposing = false;
      };
      _this.onTouchStart = function(_ref22) {
        var touches = _ref22.touches;
        var touch = touches && touches.item(0);
        if (!touch) {
          return;
        }
        _this.initialTouchX = touch.clientX;
        _this.initialTouchY = touch.clientY;
        _this.userIsDragging = false;
      };
      _this.onTouchMove = function(_ref3) {
        var touches = _ref3.touches;
        var touch = touches && touches.item(0);
        if (!touch) {
          return;
        }
        var deltaX = Math.abs(touch.clientX - _this.initialTouchX);
        var deltaY = Math.abs(touch.clientY - _this.initialTouchY);
        var moveThreshold = 5;
        _this.userIsDragging = deltaX > moveThreshold || deltaY > moveThreshold;
      };
      _this.onTouchEnd = function(event) {
        if (_this.userIsDragging) return;
        if (_this.controlRef && !_this.controlRef.contains(event.target) && _this.menuListRef && !_this.menuListRef.contains(event.target)) {
          _this.blurInput();
        }
        _this.initialTouchX = 0;
        _this.initialTouchY = 0;
      };
      _this.onControlTouchEnd = function(event) {
        if (_this.userIsDragging) return;
        _this.onControlMouseDown(event);
      };
      _this.onClearIndicatorTouchEnd = function(event) {
        if (_this.userIsDragging) return;
        _this.onClearIndicatorMouseDown(event);
      };
      _this.onDropdownIndicatorTouchEnd = function(event) {
        if (_this.userIsDragging) return;
        _this.onDropdownIndicatorMouseDown(event);
      };
      _this.handleInputChange = function(event) {
        var prevInputValue = _this.props.inputValue;
        var inputValue = event.currentTarget.value;
        _this.setState({
          inputIsHiddenAfterUpdate: false
        });
        _this.onInputChange(inputValue, {
          action: "input-change",
          prevInputValue
        });
        if (!_this.props.menuIsOpen) {
          _this.onMenuOpen();
        }
      };
      _this.onInputFocus = function(event) {
        if (_this.props.onFocus) {
          _this.props.onFocus(event);
        }
        _this.setState({
          inputIsHiddenAfterUpdate: false,
          isFocused: true
        });
        if (_this.openAfterFocus || _this.props.openMenuOnFocus) {
          _this.openMenu("first");
        }
        _this.openAfterFocus = false;
      };
      _this.onInputBlur = function(event) {
        var prevInputValue = _this.props.inputValue;
        if (_this.menuListRef && _this.menuListRef.contains(document.activeElement)) {
          _this.inputRef.focus();
          return;
        }
        if (_this.props.onBlur) {
          _this.props.onBlur(event);
        }
        _this.onInputChange("", {
          action: "input-blur",
          prevInputValue
        });
        _this.onMenuClose();
        _this.setState({
          focusedValue: null,
          isFocused: false
        });
      };
      _this.onOptionHover = function(focusedOption) {
        if (_this.blockOptionHover || _this.state.focusedOption === focusedOption) {
          return;
        }
        var options2 = _this.getFocusableOptions();
        var focusedOptionIndex = options2.indexOf(focusedOption);
        _this.setState({
          focusedOption,
          focusedOptionId: focusedOptionIndex > -1 ? _this.getFocusedOptionId(focusedOption) : null
        });
      };
      _this.shouldHideSelectedOptions = function() {
        return shouldHideSelectedOptions(_this.props);
      };
      _this.onValueInputFocus = function(e2) {
        e2.preventDefault();
        e2.stopPropagation();
        _this.focus();
      };
      _this.onKeyDown = function(event) {
        var _this$props5 = _this.props, isMulti = _this$props5.isMulti, backspaceRemovesValue = _this$props5.backspaceRemovesValue, escapeClearsValue = _this$props5.escapeClearsValue, inputValue = _this$props5.inputValue, isClearable = _this$props5.isClearable, isDisabled = _this$props5.isDisabled, menuIsOpen = _this$props5.menuIsOpen, onKeyDown = _this$props5.onKeyDown, tabSelectsValue = _this$props5.tabSelectsValue, openMenuOnFocus = _this$props5.openMenuOnFocus;
        var _this$state = _this.state, focusedOption = _this$state.focusedOption, focusedValue = _this$state.focusedValue, selectValue = _this$state.selectValue;
        if (isDisabled) return;
        if (typeof onKeyDown === "function") {
          onKeyDown(event);
          if (event.defaultPrevented) {
            return;
          }
        }
        _this.blockOptionHover = true;
        switch (event.key) {
          case "ArrowLeft":
            if (!isMulti || inputValue) return;
            _this.focusValue("previous");
            break;
          case "ArrowRight":
            if (!isMulti || inputValue) return;
            _this.focusValue("next");
            break;
          case "Delete":
          case "Backspace":
            if (inputValue) return;
            if (focusedValue) {
              _this.removeValue(focusedValue);
            } else {
              if (!backspaceRemovesValue) return;
              if (isMulti) {
                _this.popValue();
              } else if (isClearable) {
                _this.clearValue();
              }
            }
            break;
          case "Tab":
            if (_this.isComposing) return;
            if (event.shiftKey || !menuIsOpen || !tabSelectsValue || !focusedOption || // don't capture the event if the menu opens on focus and the focused
            // option is already selected; it breaks the flow of navigation
            openMenuOnFocus && _this.isOptionSelected(focusedOption, selectValue)) {
              return;
            }
            _this.selectOption(focusedOption);
            break;
          case "Enter":
            if (event.keyCode === 229) {
              break;
            }
            if (menuIsOpen) {
              if (!focusedOption) return;
              if (_this.isComposing) return;
              _this.selectOption(focusedOption);
              break;
            }
            return;
          case "Escape":
            if (menuIsOpen) {
              _this.setState({
                inputIsHiddenAfterUpdate: false
              });
              _this.onInputChange("", {
                action: "menu-close",
                prevInputValue: inputValue
              });
              _this.onMenuClose();
            } else if (isClearable && escapeClearsValue) {
              _this.clearValue();
            }
            break;
          case " ":
            if (inputValue) {
              return;
            }
            if (!menuIsOpen) {
              _this.openMenu("first");
              break;
            }
            if (!focusedOption) return;
            _this.selectOption(focusedOption);
            break;
          case "ArrowUp":
            if (menuIsOpen) {
              _this.focusOption("up");
            } else {
              _this.openMenu("last");
            }
            break;
          case "ArrowDown":
            if (menuIsOpen) {
              _this.focusOption("down");
            } else {
              _this.openMenu("first");
            }
            break;
          case "PageUp":
            if (!menuIsOpen) return;
            _this.focusOption("pageup");
            break;
          case "PageDown":
            if (!menuIsOpen) return;
            _this.focusOption("pagedown");
            break;
          case "Home":
            if (!menuIsOpen) return;
            _this.focusOption("first");
            break;
          case "End":
            if (!menuIsOpen) return;
            _this.focusOption("last");
            break;
          default:
            return;
        }
        event.preventDefault();
      };
      _this.state.instancePrefix = "react-select-" + (_this.props.instanceId || ++instanceId);
      _this.state.selectValue = cleanValue(_props.value);
      if (_props.menuIsOpen && _this.state.selectValue.length) {
        var focusableOptionsWithIds = _this.getFocusableOptionsWithIds();
        var focusableOptions = _this.buildFocusableOptions();
        var optionIndex = focusableOptions.indexOf(_this.state.selectValue[0]);
        _this.state.focusableOptionsWithIds = focusableOptionsWithIds;
        _this.state.focusedOption = focusableOptions[optionIndex];
        _this.state.focusedOptionId = getFocusedOptionId(focusableOptionsWithIds, focusableOptions[optionIndex]);
      }
      return _this;
    }
    _createClass(Select2, [{
      key: "componentDidMount",
      value: function componentDidMount() {
        this.startListeningComposition();
        this.startListeningToTouch();
        if (this.props.closeMenuOnScroll && document && document.addEventListener) {
          document.addEventListener("scroll", this.onScroll, true);
        }
        if (this.props.autoFocus) {
          this.focusInput();
        }
        if (this.props.menuIsOpen && this.state.focusedOption && this.menuListRef && this.focusedOptionRef) {
          scrollIntoView(this.menuListRef, this.focusedOptionRef);
        }
        if (isAppleDevice()) {
          this.setState({
            isAppleDevice: true
          });
        }
      }
    }, {
      key: "componentDidUpdate",
      value: function componentDidUpdate(prevProps) {
        var _this$props6 = this.props, isDisabled = _this$props6.isDisabled, menuIsOpen = _this$props6.menuIsOpen;
        var isFocused = this.state.isFocused;
        if (
          // ensure focus is restored correctly when the control becomes enabled
          isFocused && !isDisabled && prevProps.isDisabled || // ensure focus is on the Input when the menu opens
          isFocused && menuIsOpen && !prevProps.menuIsOpen
        ) {
          this.focusInput();
        }
        if (isFocused && isDisabled && !prevProps.isDisabled) {
          this.setState({
            isFocused: false
          }, this.onMenuClose);
        } else if (!isFocused && !isDisabled && prevProps.isDisabled && this.inputRef === document.activeElement) {
          this.setState({
            isFocused: true
          });
        }
        if (this.menuListRef && this.focusedOptionRef && this.scrollToFocusedOptionOnUpdate) {
          scrollIntoView(this.menuListRef, this.focusedOptionRef);
          this.scrollToFocusedOptionOnUpdate = false;
        }
      }
    }, {
      key: "componentWillUnmount",
      value: function componentWillUnmount() {
        this.stopListeningComposition();
        this.stopListeningToTouch();
        document.removeEventListener("scroll", this.onScroll, true);
      }
      // ==============================
      // Consumer Handlers
      // ==============================
    }, {
      key: "onMenuOpen",
      value: function onMenuOpen() {
        this.props.onMenuOpen();
      }
    }, {
      key: "onMenuClose",
      value: function onMenuClose() {
        this.onInputChange("", {
          action: "menu-close",
          prevInputValue: this.props.inputValue
        });
        this.props.onMenuClose();
      }
    }, {
      key: "onInputChange",
      value: function onInputChange(newValue, actionMeta) {
        this.props.onInputChange(newValue, actionMeta);
      }
      // ==============================
      // Methods
      // ==============================
    }, {
      key: "focusInput",
      value: function focusInput() {
        if (!this.inputRef) return;
        this.inputRef.focus();
      }
    }, {
      key: "blurInput",
      value: function blurInput() {
        if (!this.inputRef) return;
        this.inputRef.blur();
      }
      // aliased for consumers
    }, {
      key: "openMenu",
      value: function openMenu(focusOption) {
        var _this2 = this;
        var _this$state2 = this.state, selectValue = _this$state2.selectValue, isFocused = _this$state2.isFocused;
        var focusableOptions = this.buildFocusableOptions();
        var openAtIndex = focusOption === "first" ? 0 : focusableOptions.length - 1;
        if (!this.props.isMulti) {
          var selectedIndex = focusableOptions.indexOf(selectValue[0]);
          if (selectedIndex > -1) {
            openAtIndex = selectedIndex;
          }
        }
        this.scrollToFocusedOptionOnUpdate = !(isFocused && this.menuListRef);
        this.setState({
          inputIsHiddenAfterUpdate: false,
          focusedValue: null,
          focusedOption: focusableOptions[openAtIndex],
          focusedOptionId: this.getFocusedOptionId(focusableOptions[openAtIndex])
        }, function() {
          return _this2.onMenuOpen();
        });
      }
    }, {
      key: "focusValue",
      value: function focusValue(direction) {
        var _this$state3 = this.state, selectValue = _this$state3.selectValue, focusedValue = _this$state3.focusedValue;
        if (!this.props.isMulti) return;
        this.setState({
          focusedOption: null
        });
        var focusedIndex = selectValue.indexOf(focusedValue);
        if (!focusedValue) {
          focusedIndex = -1;
        }
        var lastIndex = selectValue.length - 1;
        var nextFocus = -1;
        if (!selectValue.length) return;
        switch (direction) {
          case "previous":
            if (focusedIndex === 0) {
              nextFocus = 0;
            } else if (focusedIndex === -1) {
              nextFocus = lastIndex;
            } else {
              nextFocus = focusedIndex - 1;
            }
            break;
          case "next":
            if (focusedIndex > -1 && focusedIndex < lastIndex) {
              nextFocus = focusedIndex + 1;
            }
            break;
        }
        this.setState({
          inputIsHidden: nextFocus !== -1,
          focusedValue: selectValue[nextFocus]
        });
      }
    }, {
      key: "focusOption",
      value: function focusOption() {
        var direction = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : "first";
        var pageSize = this.props.pageSize;
        var focusedOption = this.state.focusedOption;
        var options2 = this.getFocusableOptions();
        if (!options2.length) return;
        var nextFocus = 0;
        var focusedIndex = options2.indexOf(focusedOption);
        if (!focusedOption) {
          focusedIndex = -1;
        }
        if (direction === "up") {
          nextFocus = focusedIndex > 0 ? focusedIndex - 1 : options2.length - 1;
        } else if (direction === "down") {
          nextFocus = (focusedIndex + 1) % options2.length;
        } else if (direction === "pageup") {
          nextFocus = focusedIndex - pageSize;
          if (nextFocus < 0) nextFocus = 0;
        } else if (direction === "pagedown") {
          nextFocus = focusedIndex + pageSize;
          if (nextFocus > options2.length - 1) nextFocus = options2.length - 1;
        } else if (direction === "last") {
          nextFocus = options2.length - 1;
        }
        this.scrollToFocusedOptionOnUpdate = true;
        this.setState({
          focusedOption: options2[nextFocus],
          focusedValue: null,
          focusedOptionId: this.getFocusedOptionId(options2[nextFocus])
        });
      }
    }, {
      key: "getTheme",
      value: (
        // ==============================
        // Getters
        // ==============================
        function getTheme() {
          if (!this.props.theme) {
            return defaultTheme;
          }
          if (typeof this.props.theme === "function") {
            return this.props.theme(defaultTheme);
          }
          return _objectSpread2(_objectSpread2({}, defaultTheme), this.props.theme);
        }
      )
    }, {
      key: "getCommonProps",
      value: function getCommonProps() {
        var clearValue = this.clearValue, cx = this.cx, getStyles = this.getStyles, getClassNames = this.getClassNames, getValue2 = this.getValue, selectOption = this.selectOption, setValue = this.setValue, props = this.props;
        var isMulti = props.isMulti, isRtl = props.isRtl, options2 = props.options;
        var hasValue = this.hasValue();
        return {
          clearValue,
          cx,
          getStyles,
          getClassNames,
          getValue: getValue2,
          hasValue,
          isMulti,
          isRtl,
          options: options2,
          selectOption,
          selectProps: props,
          setValue,
          theme: this.getTheme()
        };
      }
    }, {
      key: "hasValue",
      value: function hasValue() {
        var selectValue = this.state.selectValue;
        return selectValue.length > 0;
      }
    }, {
      key: "hasOptions",
      value: function hasOptions() {
        return !!this.getFocusableOptions().length;
      }
    }, {
      key: "isClearable",
      value: function isClearable() {
        var _this$props7 = this.props, isClearable2 = _this$props7.isClearable, isMulti = _this$props7.isMulti;
        if (isClearable2 === void 0) return isMulti;
        return isClearable2;
      }
    }, {
      key: "isOptionDisabled",
      value: function isOptionDisabled3(option, selectValue) {
        return _isOptionDisabled(this.props, option, selectValue);
      }
    }, {
      key: "isOptionSelected",
      value: function isOptionSelected(option, selectValue) {
        return _isOptionSelected(this.props, option, selectValue);
      }
    }, {
      key: "filterOption",
      value: function filterOption(option, inputValue) {
        return _filterOption(this.props, option, inputValue);
      }
    }, {
      key: "formatOptionLabel",
      value: function formatOptionLabel(data, context) {
        if (typeof this.props.formatOptionLabel === "function") {
          var _inputValue = this.props.inputValue;
          var _selectValue = this.state.selectValue;
          return this.props.formatOptionLabel(data, {
            context,
            inputValue: _inputValue,
            selectValue: _selectValue
          });
        } else {
          return this.getOptionLabel(data);
        }
      }
    }, {
      key: "formatGroupLabel",
      value: function formatGroupLabel3(data) {
        return this.props.formatGroupLabel(data);
      }
      // ==============================
      // Mouse Handlers
      // ==============================
    }, {
      key: "startListeningComposition",
      value: (
        // ==============================
        // Composition Handlers
        // ==============================
        function startListeningComposition() {
          if (document && document.addEventListener) {
            document.addEventListener("compositionstart", this.onCompositionStart, false);
            document.addEventListener("compositionend", this.onCompositionEnd, false);
          }
        }
      )
    }, {
      key: "stopListeningComposition",
      value: function stopListeningComposition() {
        if (document && document.removeEventListener) {
          document.removeEventListener("compositionstart", this.onCompositionStart);
          document.removeEventListener("compositionend", this.onCompositionEnd);
        }
      }
    }, {
      key: "startListeningToTouch",
      value: (
        // ==============================
        // Touch Handlers
        // ==============================
        function startListeningToTouch() {
          if (document && document.addEventListener) {
            document.addEventListener("touchstart", this.onTouchStart, false);
            document.addEventListener("touchmove", this.onTouchMove, false);
            document.addEventListener("touchend", this.onTouchEnd, false);
          }
        }
      )
    }, {
      key: "stopListeningToTouch",
      value: function stopListeningToTouch() {
        if (document && document.removeEventListener) {
          document.removeEventListener("touchstart", this.onTouchStart);
          document.removeEventListener("touchmove", this.onTouchMove);
          document.removeEventListener("touchend", this.onTouchEnd);
        }
      }
    }, {
      key: "renderInput",
      value: (
        // ==============================
        // Renderers
        // ==============================
        function renderInput() {
          var _this$props8 = this.props, isDisabled = _this$props8.isDisabled, isSearchable = _this$props8.isSearchable, inputId = _this$props8.inputId, inputValue = _this$props8.inputValue, tabIndex = _this$props8.tabIndex, form = _this$props8.form, menuIsOpen = _this$props8.menuIsOpen, required = _this$props8.required;
          var _this$getComponents = this.getComponents(), Input2 = _this$getComponents.Input;
          var _this$state4 = this.state, inputIsHidden = _this$state4.inputIsHidden, ariaSelection = _this$state4.ariaSelection;
          var commonProps = this.commonProps;
          var id = inputId || this.getElementId("input");
          var ariaAttributes = _objectSpread2(_objectSpread2(_objectSpread2({
            "aria-autocomplete": "list",
            "aria-expanded": menuIsOpen,
            "aria-haspopup": true,
            "aria-errormessage": this.props["aria-errormessage"],
            "aria-invalid": this.props["aria-invalid"],
            "aria-label": this.props["aria-label"],
            "aria-labelledby": this.props["aria-labelledby"],
            "aria-required": required,
            role: "combobox",
            "aria-activedescendant": this.state.isAppleDevice ? void 0 : this.state.focusedOptionId || ""
          }, menuIsOpen && {
            "aria-controls": this.getElementId("listbox")
          }), !isSearchable && {
            "aria-readonly": true
          }), this.hasValue() ? (ariaSelection === null || ariaSelection === void 0 ? void 0 : ariaSelection.action) === "initial-input-focus" && {
            "aria-describedby": this.getElementId("live-region")
          } : {
            "aria-describedby": this.getElementId("placeholder")
          });
          if (!isSearchable) {
            return /* @__PURE__ */ React__namespace.createElement(DummyInput, _extends({
              id,
              innerRef: this.getInputRef,
              onBlur: this.onInputBlur,
              onChange: noop,
              onFocus: this.onInputFocus,
              disabled: isDisabled,
              tabIndex,
              inputMode: "none",
              form,
              value: ""
            }, ariaAttributes));
          }
          return /* @__PURE__ */ React__namespace.createElement(Input2, _extends({}, commonProps, {
            autoCapitalize: "none",
            autoComplete: "off",
            autoCorrect: "off",
            id,
            innerRef: this.getInputRef,
            isDisabled,
            isHidden: inputIsHidden,
            onBlur: this.onInputBlur,
            onChange: this.handleInputChange,
            onFocus: this.onInputFocus,
            spellCheck: "false",
            tabIndex,
            form,
            type: "text",
            value: inputValue
          }, ariaAttributes));
        }
      )
    }, {
      key: "renderPlaceholderOrValue",
      value: function renderPlaceholderOrValue() {
        var _this3 = this;
        var _this$getComponents2 = this.getComponents(), MultiValue2 = _this$getComponents2.MultiValue, MultiValueContainer2 = _this$getComponents2.MultiValueContainer, MultiValueLabel2 = _this$getComponents2.MultiValueLabel, MultiValueRemove2 = _this$getComponents2.MultiValueRemove, SingleValue2 = _this$getComponents2.SingleValue, Placeholder2 = _this$getComponents2.Placeholder;
        var commonProps = this.commonProps;
        var _this$props9 = this.props, controlShouldRenderValue = _this$props9.controlShouldRenderValue, isDisabled = _this$props9.isDisabled, isMulti = _this$props9.isMulti, inputValue = _this$props9.inputValue, placeholder = _this$props9.placeholder;
        var _this$state5 = this.state, selectValue = _this$state5.selectValue, focusedValue = _this$state5.focusedValue, isFocused = _this$state5.isFocused;
        if (!this.hasValue() || !controlShouldRenderValue) {
          return inputValue ? null : /* @__PURE__ */ React__namespace.createElement(Placeholder2, _extends({}, commonProps, {
            key: "placeholder",
            isDisabled,
            isFocused,
            innerProps: {
              id: this.getElementId("placeholder")
            }
          }), placeholder);
        }
        if (isMulti) {
          return selectValue.map(function(opt, index2) {
            var isOptionFocused = opt === focusedValue;
            var key = "".concat(_this3.getOptionLabel(opt), "-").concat(_this3.getOptionValue(opt));
            return /* @__PURE__ */ React__namespace.createElement(MultiValue2, _extends({}, commonProps, {
              components: {
                Container: MultiValueContainer2,
                Label: MultiValueLabel2,
                Remove: MultiValueRemove2
              },
              isFocused: isOptionFocused,
              isDisabled,
              key,
              index: index2,
              removeProps: {
                onClick: function onClick() {
                  return _this3.removeValue(opt);
                },
                onTouchEnd: function onTouchEnd() {
                  return _this3.removeValue(opt);
                },
                onMouseDown: function onMouseDown(e2) {
                  e2.preventDefault();
                }
              },
              data: opt
            }), _this3.formatOptionLabel(opt, "value"));
          });
        }
        if (inputValue) {
          return null;
        }
        var singleValue = selectValue[0];
        return /* @__PURE__ */ React__namespace.createElement(SingleValue2, _extends({}, commonProps, {
          data: singleValue,
          isDisabled
        }), this.formatOptionLabel(singleValue, "value"));
      }
    }, {
      key: "renderClearIndicator",
      value: function renderClearIndicator() {
        var _this$getComponents3 = this.getComponents(), ClearIndicator2 = _this$getComponents3.ClearIndicator;
        var commonProps = this.commonProps;
        var _this$props10 = this.props, isDisabled = _this$props10.isDisabled, isLoading = _this$props10.isLoading;
        var isFocused = this.state.isFocused;
        if (!this.isClearable() || !ClearIndicator2 || isDisabled || !this.hasValue() || isLoading) {
          return null;
        }
        var innerProps = {
          onMouseDown: this.onClearIndicatorMouseDown,
          onTouchEnd: this.onClearIndicatorTouchEnd,
          "aria-hidden": "true"
        };
        return /* @__PURE__ */ React__namespace.createElement(ClearIndicator2, _extends({}, commonProps, {
          innerProps,
          isFocused
        }));
      }
    }, {
      key: "renderLoadingIndicator",
      value: function renderLoadingIndicator() {
        var _this$getComponents4 = this.getComponents(), LoadingIndicator2 = _this$getComponents4.LoadingIndicator;
        var commonProps = this.commonProps;
        var _this$props11 = this.props, isDisabled = _this$props11.isDisabled, isLoading = _this$props11.isLoading;
        var isFocused = this.state.isFocused;
        if (!LoadingIndicator2 || !isLoading) return null;
        var innerProps = {
          "aria-hidden": "true"
        };
        return /* @__PURE__ */ React__namespace.createElement(LoadingIndicator2, _extends({}, commonProps, {
          innerProps,
          isDisabled,
          isFocused
        }));
      }
    }, {
      key: "renderIndicatorSeparator",
      value: function renderIndicatorSeparator() {
        var _this$getComponents5 = this.getComponents(), DropdownIndicator2 = _this$getComponents5.DropdownIndicator, IndicatorSeparator2 = _this$getComponents5.IndicatorSeparator;
        if (!DropdownIndicator2 || !IndicatorSeparator2) return null;
        var commonProps = this.commonProps;
        var isDisabled = this.props.isDisabled;
        var isFocused = this.state.isFocused;
        return /* @__PURE__ */ React__namespace.createElement(IndicatorSeparator2, _extends({}, commonProps, {
          isDisabled,
          isFocused
        }));
      }
    }, {
      key: "renderDropdownIndicator",
      value: function renderDropdownIndicator() {
        var _this$getComponents6 = this.getComponents(), DropdownIndicator2 = _this$getComponents6.DropdownIndicator;
        if (!DropdownIndicator2) return null;
        var commonProps = this.commonProps;
        var isDisabled = this.props.isDisabled;
        var isFocused = this.state.isFocused;
        var innerProps = {
          onMouseDown: this.onDropdownIndicatorMouseDown,
          onTouchEnd: this.onDropdownIndicatorTouchEnd,
          "aria-hidden": "true"
        };
        return /* @__PURE__ */ React__namespace.createElement(DropdownIndicator2, _extends({}, commonProps, {
          innerProps,
          isDisabled,
          isFocused
        }));
      }
    }, {
      key: "renderMenu",
      value: function renderMenu() {
        var _this4 = this;
        var _this$getComponents7 = this.getComponents(), Group2 = _this$getComponents7.Group, GroupHeading2 = _this$getComponents7.GroupHeading, Menu2 = _this$getComponents7.Menu, MenuList2 = _this$getComponents7.MenuList, MenuPortal2 = _this$getComponents7.MenuPortal, LoadingMessage2 = _this$getComponents7.LoadingMessage, NoOptionsMessage2 = _this$getComponents7.NoOptionsMessage, Option2 = _this$getComponents7.Option;
        var commonProps = this.commonProps;
        var focusedOption = this.state.focusedOption;
        var _this$props12 = this.props, captureMenuScroll = _this$props12.captureMenuScroll, inputValue = _this$props12.inputValue, isLoading = _this$props12.isLoading, loadingMessage2 = _this$props12.loadingMessage, minMenuHeight = _this$props12.minMenuHeight, maxMenuHeight = _this$props12.maxMenuHeight, menuIsOpen = _this$props12.menuIsOpen, menuPlacement = _this$props12.menuPlacement, menuPosition = _this$props12.menuPosition, menuPortalTarget = _this$props12.menuPortalTarget, menuShouldBlockScroll = _this$props12.menuShouldBlockScroll, menuShouldScrollIntoView = _this$props12.menuShouldScrollIntoView, noOptionsMessage2 = _this$props12.noOptionsMessage, onMenuScrollToTop = _this$props12.onMenuScrollToTop, onMenuScrollToBottom = _this$props12.onMenuScrollToBottom;
        if (!menuIsOpen) return null;
        var render = function render2(props, id) {
          var type = props.type, data = props.data, isDisabled = props.isDisabled, isSelected = props.isSelected, label = props.label, value = props.value;
          var isFocused = focusedOption === data;
          var onHover = isDisabled ? void 0 : function() {
            return _this4.onOptionHover(data);
          };
          var onSelect = isDisabled ? void 0 : function() {
            return _this4.selectOption(data);
          };
          var optionId = "".concat(_this4.getElementId("option"), "-").concat(id);
          var innerProps = {
            id: optionId,
            onClick: onSelect,
            onMouseMove: onHover,
            onMouseOver: onHover,
            tabIndex: -1,
            role: "option",
            "aria-selected": _this4.state.isAppleDevice ? void 0 : isSelected
            // is not supported on Apple devices
          };
          return /* @__PURE__ */ React__namespace.createElement(Option2, _extends({}, commonProps, {
            innerProps,
            data,
            isDisabled,
            isSelected,
            key: optionId,
            label,
            type,
            value,
            isFocused,
            innerRef: isFocused ? _this4.getFocusedOptionRef : void 0
          }), _this4.formatOptionLabel(props.data, "menu"));
        };
        var menuUI;
        if (this.hasOptions()) {
          menuUI = this.getCategorizedOptions().map(function(item) {
            if (item.type === "group") {
              var _data = item.data, options2 = item.options, groupIndex = item.index;
              var groupId = "".concat(_this4.getElementId("group"), "-").concat(groupIndex);
              var headingId = "".concat(groupId, "-heading");
              return /* @__PURE__ */ React__namespace.createElement(Group2, _extends({}, commonProps, {
                key: groupId,
                data: _data,
                options: options2,
                Heading: GroupHeading2,
                headingProps: {
                  id: headingId,
                  data: item.data
                },
                label: _this4.formatGroupLabel(item.data)
              }), item.options.map(function(option) {
                return render(option, "".concat(groupIndex, "-").concat(option.index));
              }));
            } else if (item.type === "option") {
              return render(item, "".concat(item.index));
            }
          });
        } else if (isLoading) {
          var message = loadingMessage2({
            inputValue
          });
          if (message === null) return null;
          menuUI = /* @__PURE__ */ React__namespace.createElement(LoadingMessage2, commonProps, message);
        } else {
          var _message = noOptionsMessage2({
            inputValue
          });
          if (_message === null) return null;
          menuUI = /* @__PURE__ */ React__namespace.createElement(NoOptionsMessage2, commonProps, _message);
        }
        var menuPlacementProps = {
          minMenuHeight,
          maxMenuHeight,
          menuPlacement,
          menuPosition,
          menuShouldScrollIntoView
        };
        var menuElement = /* @__PURE__ */ React__namespace.createElement(MenuPlacer, _extends({}, commonProps, menuPlacementProps), function(_ref4) {
          var ref = _ref4.ref, _ref4$placerProps = _ref4.placerProps, placement = _ref4$placerProps.placement, maxHeight = _ref4$placerProps.maxHeight;
          return /* @__PURE__ */ React__namespace.createElement(Menu2, _extends({}, commonProps, menuPlacementProps, {
            innerRef: ref,
            innerProps: {
              onMouseDown: _this4.onMenuMouseDown,
              onMouseMove: _this4.onMenuMouseMove
            },
            isLoading,
            placement
          }), /* @__PURE__ */ React__namespace.createElement(ScrollManager, {
            captureEnabled: captureMenuScroll,
            onTopArrive: onMenuScrollToTop,
            onBottomArrive: onMenuScrollToBottom,
            lockEnabled: menuShouldBlockScroll
          }, function(scrollTargetRef) {
            return /* @__PURE__ */ React__namespace.createElement(MenuList2, _extends({}, commonProps, {
              innerRef: function innerRef(instance) {
                _this4.getMenuListRef(instance);
                scrollTargetRef(instance);
              },
              innerProps: {
                role: "listbox",
                "aria-multiselectable": commonProps.isMulti,
                id: _this4.getElementId("listbox")
              },
              isLoading,
              maxHeight,
              focusedOption
            }), menuUI);
          }));
        });
        return menuPortalTarget || menuPosition === "fixed" ? /* @__PURE__ */ React__namespace.createElement(MenuPortal2, _extends({}, commonProps, {
          appendTo: menuPortalTarget,
          controlElement: this.controlRef,
          menuPlacement,
          menuPosition
        }), menuElement) : menuElement;
      }
    }, {
      key: "renderFormField",
      value: function renderFormField() {
        var _this5 = this;
        var _this$props13 = this.props, delimiter2 = _this$props13.delimiter, isDisabled = _this$props13.isDisabled, isMulti = _this$props13.isMulti, name = _this$props13.name, required = _this$props13.required;
        var selectValue = this.state.selectValue;
        if (required && !this.hasValue() && !isDisabled) {
          return /* @__PURE__ */ React__namespace.createElement(RequiredInput$1, {
            name,
            onFocus: this.onValueInputFocus
          });
        }
        if (!name || isDisabled) return;
        if (isMulti) {
          if (delimiter2) {
            var value = selectValue.map(function(opt) {
              return _this5.getOptionValue(opt);
            }).join(delimiter2);
            return /* @__PURE__ */ React__namespace.createElement("input", {
              name,
              type: "hidden",
              value
            });
          } else {
            var input = selectValue.length > 0 ? selectValue.map(function(opt, i2) {
              return /* @__PURE__ */ React__namespace.createElement("input", {
                key: "i-".concat(i2),
                name,
                type: "hidden",
                value: _this5.getOptionValue(opt)
              });
            }) : /* @__PURE__ */ React__namespace.createElement("input", {
              name,
              type: "hidden",
              value: ""
            });
            return /* @__PURE__ */ React__namespace.createElement("div", null, input);
          }
        } else {
          var _value = selectValue[0] ? this.getOptionValue(selectValue[0]) : "";
          return /* @__PURE__ */ React__namespace.createElement("input", {
            name,
            type: "hidden",
            value: _value
          });
        }
      }
    }, {
      key: "renderLiveRegion",
      value: function renderLiveRegion() {
        var commonProps = this.commonProps;
        var _this$state6 = this.state, ariaSelection = _this$state6.ariaSelection, focusedOption = _this$state6.focusedOption, focusedValue = _this$state6.focusedValue, isFocused = _this$state6.isFocused, selectValue = _this$state6.selectValue;
        var focusableOptions = this.getFocusableOptions();
        return /* @__PURE__ */ React__namespace.createElement(LiveRegion$1, _extends({}, commonProps, {
          id: this.getElementId("live-region"),
          ariaSelection,
          focusedOption,
          focusedValue,
          isFocused,
          selectValue,
          focusableOptions,
          isAppleDevice: this.state.isAppleDevice
        }));
      }
    }, {
      key: "render",
      value: function render() {
        var _this$getComponents8 = this.getComponents(), Control2 = _this$getComponents8.Control, IndicatorsContainer2 = _this$getComponents8.IndicatorsContainer, SelectContainer2 = _this$getComponents8.SelectContainer, ValueContainer2 = _this$getComponents8.ValueContainer;
        var _this$props14 = this.props, className = _this$props14.className, id = _this$props14.id, isDisabled = _this$props14.isDisabled, menuIsOpen = _this$props14.menuIsOpen;
        var isFocused = this.state.isFocused;
        var commonProps = this.commonProps = this.getCommonProps();
        return /* @__PURE__ */ React__namespace.createElement(SelectContainer2, _extends({}, commonProps, {
          className,
          innerProps: {
            id,
            onKeyDown: this.onKeyDown
          },
          isDisabled,
          isFocused
        }), this.renderLiveRegion(), /* @__PURE__ */ React__namespace.createElement(Control2, _extends({}, commonProps, {
          innerRef: this.getControlRef,
          innerProps: {
            onMouseDown: this.onControlMouseDown,
            onTouchEnd: this.onControlTouchEnd
          },
          isDisabled,
          isFocused,
          menuIsOpen
        }), /* @__PURE__ */ React__namespace.createElement(ValueContainer2, _extends({}, commonProps, {
          isDisabled
        }), this.renderPlaceholderOrValue(), this.renderInput()), /* @__PURE__ */ React__namespace.createElement(IndicatorsContainer2, _extends({}, commonProps, {
          isDisabled
        }), this.renderClearIndicator(), this.renderLoadingIndicator(), this.renderIndicatorSeparator(), this.renderDropdownIndicator())), this.renderMenu(), this.renderFormField());
      }
    }], [{
      key: "getDerivedStateFromProps",
      value: function getDerivedStateFromProps(props, state) {
        var prevProps = state.prevProps, clearFocusValueOnUpdate = state.clearFocusValueOnUpdate, inputIsHiddenAfterUpdate = state.inputIsHiddenAfterUpdate, ariaSelection = state.ariaSelection, isFocused = state.isFocused, prevWasFocused = state.prevWasFocused, instancePrefix = state.instancePrefix;
        var options2 = props.options, value = props.value, menuIsOpen = props.menuIsOpen, inputValue = props.inputValue, isMulti = props.isMulti;
        var selectValue = cleanValue(value);
        var newMenuOptionsState = {};
        if (prevProps && (value !== prevProps.value || options2 !== prevProps.options || menuIsOpen !== prevProps.menuIsOpen || inputValue !== prevProps.inputValue)) {
          var focusableOptions = menuIsOpen ? buildFocusableOptions(props, selectValue) : [];
          var focusableOptionsWithIds = menuIsOpen ? buildFocusableOptionsWithIds(buildCategorizedOptions(props, selectValue), "".concat(instancePrefix, "-option")) : [];
          var focusedValue = clearFocusValueOnUpdate ? getNextFocusedValue(state, selectValue) : null;
          var focusedOption = getNextFocusedOption(state, focusableOptions);
          var focusedOptionId = getFocusedOptionId(focusableOptionsWithIds, focusedOption);
          newMenuOptionsState = {
            selectValue,
            focusedOption,
            focusedOptionId,
            focusableOptionsWithIds,
            focusedValue,
            clearFocusValueOnUpdate: false
          };
        }
        var newInputIsHiddenState = inputIsHiddenAfterUpdate != null && props !== prevProps ? {
          inputIsHidden: inputIsHiddenAfterUpdate,
          inputIsHiddenAfterUpdate: void 0
        } : {};
        var newAriaSelection = ariaSelection;
        var hasKeptFocus = isFocused && prevWasFocused;
        if (isFocused && !hasKeptFocus) {
          newAriaSelection = {
            value: valueTernary(isMulti, selectValue, selectValue[0] || null),
            options: selectValue,
            action: "initial-input-focus"
          };
          hasKeptFocus = !prevWasFocused;
        }
        if ((ariaSelection === null || ariaSelection === void 0 ? void 0 : ariaSelection.action) === "initial-input-focus") {
          newAriaSelection = null;
        }
        return _objectSpread2(_objectSpread2(_objectSpread2({}, newMenuOptionsState), newInputIsHiddenState), {}, {
          prevProps: props,
          ariaSelection: newAriaSelection,
          prevWasFocused: hasKeptFocus
        });
      }
    }]);
    return Select2;
  }(React.Component);
  Select$1.defaultProps = defaultProps;
  var StateManagedSelect = /* @__PURE__ */ React.forwardRef(function(props, ref) {
    var baseSelectProps = useStateManager(props);
    return /* @__PURE__ */ React__namespace.createElement(Select$1, _extends({
      ref
    }, baseSelectProps));
  });
  var StateManagedSelect$1 = StateManagedSelect;
  const CountryFlag = (props) => {
    const { countryId, style } = props;
    if (!countryId) return null;
    return /* @__PURE__ */ React.createElement(
      "img",
      {
        style: __spreadValues({ height: "16px", width: "23px" }, style || {}),
        src: `https://u.alicdn.com/mobile/g/common/flags/1.0.0/assets/${countryId.toLowerCase()}.png`
      }
    );
  };
  const getValue = (options2, value) => {
    if (!value) return null;
    const target = (options2 || []).reduce((buf, cur) => {
      return [...buf, ...cur.options || []];
    }, []).find((item) => item.value === value);
    return target || null;
  };
  const countryItemRender = (item) => {
    const { value, label, selectOption } = item;
    return /* @__PURE__ */ React.createElement(
      "div",
      {
        className: "crated-header-ship-to-country-item",
        onClick: (e2) => {
          e2.stopPropagation();
          selectOption({ label, value });
        }
      },
      /* @__PURE__ */ React.createElement(CountryFlag, { style: { marginInlineEnd: "8px", marginInlineStart: "2px" }, countryId: value }),
      label
    );
  };
  const Select = (props) => {
    const _a = props, { options: options2, value, onChange, onMenuOpen, onMenuClose } = _a, others = __objRest(_a, ["options", "value", "onChange", "onMenuOpen", "onMenuClose"]);
    const current = getValue(options2, value);
    return /* @__PURE__ */ React.createElement(
      StateManagedSelect$1,
      __spreadProps(__spreadValues({}, others), {
        options: options2,
        value: current,
        defaultValue: current,
        onChange: (target) => {
          onChange((target == null ? void 0 : target.value) || null);
        },
        onMenuOpen,
        onMenuClose,
        menuPosition: "fixed",
        components: {
          Option: (optionProps) => countryItemRender(optionProps),
          Control: (_b) => {
            var _c = _b, { children } = _c, controlProps = __objRest(_c, ["children"]);
            return /* @__PURE__ */ React.createElement(components.Control, __spreadValues({}, controlProps), value ? /* @__PURE__ */ React.createElement(CountryFlag, { style: { marginInlineStart: "14px" }, countryId: value }) : null, children);
          }
        }
      })
    );
  };
  const i18nBase = {
    Title: "Choose your location",
    Desc: "Delivery options and fees may vary based on your locations",
    SeeAll: "See all addresses",
    Add: "Add an address",
    Save: "Save",
    PopularCountry: "Popular countries/regions",
    AllCountries: "All countries/regions",
    ZipPlaceholder: "Enter city or zip",
    ShipToTitle: "Ship to: ",
    SignInTips: "Sign in to see your address"
  };
  const win = typeof window === "undefined" ? {} : window;
  const i18n = (win == null ? void 0 : win.i18n) || i18nBase;
  const i18nAllMap = {
    "ru_RU": {
      "Default": "Адрес доставки по умолчанию"
    },
    "it_IT": {
      "Default": "Indirizzo di spedizione predefinito"
    },
    "tr_TR": {
      "Default": "Varsayılan gönderim adresi"
    },
    "hi_IN": {
      "Default": "डिफ़ॉल्ट शिपिंग पता"
    },
    "th_TH": {
      "Default": "ที่อยู่จัดส่งเริ่มต้น"
    },
    "fr_FR": {
      "Default": "Adresse de livraison par défaut"
    },
    "ja_JP": {
      "Default": "デフォルトの配送先住所"
    },
    "in_ID": {
      "Default": "Alamat utama"
    },
    "de_DE": {
      "Default": "Standard-Versandadresse"
    },
    "ar_SA": {
      "Default": "عنوان الشحن الافتراضي"
    },
    "zh_TW": {
      "Default": "預設收件地址"
    },
    "es_ES": {
      "Default": "Dirección de envío predeterminada"
    },
    "nl_NL": {
      "Default": "Standaard verzendadres"
    },
    "bn_IN": {
      "Default": "##@@@ta.order.com.shippingAddressForm.tags.DEFAULT##trade-contract@@@##"
    },
    "iw_IL": {
      "Default": "כתובת ברירת מחדל למשלוח"
    },
    "vi_VN": {
      "Default": "Địa chỉ vận chuyển mặc định"
    },
    "ko_KR": {
      "Default": "기본 배송 주소"
    },
    "en_US": {
      "Default": "Default shipping address"
    },
    "zh_CN": {
      "Default": "默认收货地址"
    },
    "pt_PT": {
      "Default": "Endereço de Entrega Padrão"
    }
  };
  const lang = getLatestCookieData().language;
  const i18nMap = i18nAllMap[lang] || i18nAllMap.en_US;
  function log(key, params) {
    try {
      const { goldlog } = window;
      if (goldlog && goldlog.record) {
        const querys = Object.keys(params || {}).map((k2) => {
          return `${k2}=${params == null ? void 0 : params[k2]}`;
        });
        querys.push(`st_page_id=${window.dmtrack_pageid || ""}`);
        goldlog.record(key, "EXP", querys.join("&"));
      }
    } catch (e2) {
    }
  }
  function logSyncCookieError() {
    logError({
      api: "syncCookieShipTo",
      errorType: "JSONP"
    });
  }
  function logError(params) {
    log("/sc.sc_header_footer.error", params);
  }
  function logAdd() {
    log("/sc.sc_header_footer_ship_to.add");
  }
  function logAllAddress() {
    log("/sc.sc_header_footer_ship_to.all_address");
  }
  function logSelectItem(params) {
    log("/sc.sc_header_footer_ship_to.select", params);
  }
  function logSavetem(params) {
    log("/sc.sc_header_footer_ship_to.save", params);
  }
  function logLogin() {
    log("/sc.sc_header_footer_ship_to.login");
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
        } catch (e2) {
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
        var options2 = arguments.length <= 1 || arguments[1] === void 0 ? {} : arguments[1];
        var url = _url;
        var timeout = options2.timeout || defaultOptions.timeout;
        var jsonpCallback = options2.jsonpCallback || defaultOptions.jsonpCallback;
        var timeoutId = void 0;
        return new Promise(function(resolve, reject) {
          var callbackFunction = options2.jsonpCallbackFunction || generateCallbackFunction();
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
          if (options2.charset) {
            jsonpScript.setAttribute("charset", options2.charset);
          }
          if (options2.nonce) {
            jsonpScript.setAttribute("nonce", options2.nonce);
          }
          if (options2.referrerPolicy) {
            jsonpScript.setAttribute("referrerPolicy", options2.referrerPolicy);
          }
          if (options2.crossorigin) {
            jsonpScript.setAttribute("crossorigin", typeof options2.crossorigin === "string" ? options2.crossorigin : "anonymous");
          }
          var fp = options2.fetchPriority;
          if (fp === "high" || fp === "low" || fp === "auto") {
            jsonpScript.setAttribute("fetchPriority", fp);
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
  const Fetch_Domain = `//ug.alibaba.${getTopLevelDomain()}/`;
  function getTopLevelDomain() {
    var _a;
    const hostTemps = (_a = location == null ? void 0 : location.host) == null ? void 0 : _a.match(/(.*?).alibaba\.(.*?)$/);
    if (hostTemps && hostTemps.length >= 3) {
      return hostTemps[2];
    } else {
      return "com";
    }
  }
  const saveLocalData = (params) => {
    let fetchSaveUrl = `${Fetch_Domain}api/ship/write`;
    Object.keys(params).forEach((key) => {
      const value = params[key];
      if (value) {
        fetchSaveUrl += `${fetchSaveUrl.indexOf("?") > -1 ? "&" : "?"}${key}=${value}`;
      }
    });
    return fetchJsonp(fetchSaveUrl).then((res) => res.json()).then((res) => {
      if (res.data && res.code === 200) {
        location.reload();
      } else {
        logSyncCookieError();
      }
    }).catch(() => {
      logSyncCookieError();
    });
  };
  const queryList = () => __async(this, null, function* () {
    return fetchJsonp(`${Fetch_Domain}api/ship/queryShipToPanelAddressList?ctoken=${getCtoken()}`).then((res) => res.json()).then((res) => {
      if ((res == null ? void 0 : res.code) === 200 && res.data) {
        return res.data;
      } else {
        logError({
          api: "ajaxShipToList",
          errorType: "JSONP"
        });
      }
    }).catch(() => {
      logError({
        api: "ajaxShipToList",
        errorType: "JSONP"
      });
    });
  });
  const queryCountryCurrency = () => __async(this, null, function* () {
    return fetchJsonp(`${Fetch_Domain}api/ship/read`).then((res) => res.json()).then((res) => res.data);
  });
  function ShipTo({
    localData,
    onVisibleChange,
    i18n: propsI18N,
    onMenuStateChange
  }) {
    var _a;
    const i18n$1 = propsI18N || i18n;
    const popupRef = React.useRef(null);
    const [loading, setLoading] = React.useState(true);
    const [isLogin, setIsLogin] = React.useState(false);
    const [list, setList] = React.useState([]);
    const [selectAddressId, setSelectAddressId] = React.useState(-1);
    const [defaultAddress, setDefaultAddressId] = React.useState(-1);
    const [countryDataSource, setCountryDataSource] = React.useState([]);
    const [zip, setZip] = React.useState("");
    const [country, setCountry] = React.useState(null);
    const [isInvalid, setIsInvalid] = React.useState(false);
    const [addressInvalid, setAddressInvalid] = React.useState(false);
    const [countryInvalid, setCountryInvalid] = React.useState(false);
    const isValidList = Array.isArray(list) && list.length > 0;
    React.useEffect(() => {
      initLocalData();
      initAddressList();
    }, [localData]);
    const onSelectItem = (item) => {
      setSelectAddressId(item.appAddressId);
      setCountry(null);
      setZip("");
      logSelectItem({
        country: item.appCountry,
        zip: item.appZipCode
      });
      setAddressInvalid(false);
      setCountryInvalid(false);
    };
    const onSave = () => __async(this, null, function* () {
      if (!country && selectAddressId === -1) {
        setCountryInvalid(true);
        return;
      }
      if (isInvalid || addressInvalid) return;
      setLoading(true);
      let params = {
        localCountry: null
      };
      if (selectAddressId === -1) {
        params = {
          localCountry: country,
          localZipCode: zip
        };
      } else {
        const target = list.find((item) => item.appAddressId === selectAddressId);
        if (target) {
          params = {
            localCountry: target.appCountry,
            localZipCode: target.appZipCode,
            localAddressId: target.appAddressId
          };
        }
      }
      if (selectAddressId === -1 && !params.localCountry && !params.localZipCode) return;
      yield saveLocalData(params);
      setLoading(false);
      logSavetem(params);
      onVisibleChange == null ? void 0 : onVisibleChange(false);
    });
    const handleLogin = () => {
      var _a2, _b;
      const xman = (_a2 = window.loadXman) == null ? void 0 : _a2.call(window, {
        signInSuccess: () => {
        }
      });
      if (xman) {
        (_b = xman.show) == null ? void 0 : _b.call(xman);
      } else {
        window.open("https://login.alibaba.com?tracelog=purchase_cart");
      }
      logLogin();
    };
    const handleCountryChange = (nextCountry) => {
      setCountry(nextCountry);
      setSelectAddressId(-1);
      setAddressInvalid(false);
      setCountryInvalid(false);
    };
    const handleZipChange = (e2) => {
      setZip(e2.target.value);
      setSelectAddressId(-1);
      setAddressInvalid(false);
    };
    const formatCountryItem = function(item) {
      const { code, name } = item;
      return __spreadProps(__spreadValues({}, item), {
        label: name,
        value: code
      });
    };
    const initLocalData = () => __async(this, null, function* () {
      const {
        countryModule,
        currentlySelectedLocalCountry = DEFAULT_COUNTRY,
        currentlySelectedLocalAddressId,
        currentlySelectedLocalZipCode = ""
      } = localData || (yield queryCountryCurrency()) || {};
      handleSetCountryList(countryModule);
      if (!currentlySelectedLocalAddressId) {
        setCountry(currentlySelectedLocalCountry);
        setZip(currentlySelectedLocalZipCode);
      }
    });
    const initAddressList = () => __async(this, null, function* () {
      var _a2, _b;
      const loginRes = getIsLoggedIn();
      setIsLogin(loginRes);
      if (loginRes) {
        let addressList = [];
        if ((_a2 = window == null ? void 0 : window.headerShipToAddressData) == null ? void 0 : _a2.addressList) {
          addressList = (_b = window == null ? void 0 : window.headerShipToAddressData) == null ? void 0 : _b.addressList;
        } else {
          const listRes = yield queryList();
          window.headerShipToAddressData = listRes;
          addressList = (listRes == null ? void 0 : listRes.addressList) || [];
        }
        setList(addressList || []);
        addressList.forEach((item) => {
          if (item.selected) setSelectAddressId(item.appAddressId);
          if (item.isDefault) setDefaultAddressId(item.appAddressId);
        });
        new Image().src = "https://logistics.alibaba.com/luyou/shipto/list.htm";
      }
      setLoading(false);
    });
    const handleSetCountryList = (countryModule) => {
      const countryList = [];
      const { popularCountryList, allCountryList } = countryModule || {};
      if (popularCountryList == null ? void 0 : popularCountryList.length) {
        countryList.push({
          label: i18n$1.PopularCountry,
          options: popularCountryList.map(
            formatCountryItem
          )
        });
      }
      if (allCountryList == null ? void 0 : allCountryList.length) {
        countryList.push({
          label: i18n$1.AllCountries,
          options: allCountryList.filter((allItem) => {
            return !(popularCountryList || []).some(
              (popularItem) => popularItem.code === allItem.code
            );
          }).map(formatCountryItem)
        });
      }
      setCountryDataSource(countryList);
    };
    return /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to" }, /* @__PURE__ */ React.createElement("b", { className: "crated-header-ship-to-title" }, i18n$1.Title), /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-desc" }, i18n$1.Desc), loading && isLogin ? /* @__PURE__ */ React.createElement(Loading, null) : null, !isLogin ? /* @__PURE__ */ React.createElement("a", { className: "crated-header-ship-to-sign-in", "data-role": "sign-in", onClick: handleLogin }, i18n$1.SignInTips) : /* @__PURE__ */ React.createElement(React.Fragment, null, (_a = list == null ? void 0 : list.slice(0, 3)) == null ? void 0 : _a.map((item) => {
      return /* @__PURE__ */ React.createElement("div", { className: "address-item-container", key: item.appAddressId }, /* @__PURE__ */ React.createElement(
        "div",
        {
          "data-id": `${item.appAddressId}`,
          className: `crated-header-ship-to-item ${item.appAddressId === selectAddressId ? "current" : ""}`,
          onClick: () => {
            onSelectItem(item);
          }
        },
        /* @__PURE__ */ React.createElement("div", null, /* @__PURE__ */ React.createElement("div", null, /* @__PURE__ */ React.createElement("b", null, item.contactName, " "), item.displayAddress)),
        item.appAddressId === defaultAddress ? /* @__PURE__ */ React.createElement("span", { className: "crated-header-ship-to-item-default" }, i18nMap.Default) : null,
        addressInvalid && item.appAddressId === selectAddressId && /* @__PURE__ */ React.createElement("span", { className: "ship-to-invalid-span", style: { marginTop: "12px" } }, /* @__PURE__ */ React.createElement("img", { src: "https://img.alicdn.com/imgextra/i3/O1CN01hhrXZV29AQ9C7DoXD_!!6000000008027-2-tps-32-32.png" }), i18n$1[`sctnh.header_shipto_address_invalid_${item.appCountry}`] || i18n$1["sctnh.header_shipto_address_invalid"] || 'Invalid ZIP code. Example of the correct format: "1000".Please type in a new zip code below.')
      ));
    }), isValidList && /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-action-container" }, /* @__PURE__ */ React.createElement(
      "a",
      {
        href: VALID_LIST_URL,
        target: "_blank",
        role: "see-all-address",
        className: "crated-header-ship-to-action",
        onClick: logAllAddress,
        rel: "noreferrer"
      },
      i18n$1.SeeAll
    ), /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-separator" }), /* @__PURE__ */ React.createElement(
      "a",
      {
        href: VALID_ADD_URL,
        target: "_blank",
        role: "add-address",
        className: "crated-header-ship-to-action",
        onClick: logAdd,
        rel: "noreferrer"
      },
      i18n$1.Add
    ))), !isValidList && isLogin ? /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-no-data-container", style: { marginTop: "12px" } }, /* @__PURE__ */ React.createElement(
      "a",
      {
        href: VALID_ADD_URL,
        target: "_blank",
        role: "add-address",
        className: "crated-header-ship-to-action-btn",
        onClick: logAdd,
        rel: "noreferrer"
      },
      i18n$1.Add
    )) : null, /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-dash-wrapper" }, /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-dash-line" }), /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-dash-line-text-wrapper" }, /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-dash-line-text" }, i18n$1["sctnh.header_shipto_or"] || "Or"))), /* @__PURE__ */ React.createElement(
      Select,
      {
        value: country,
        onChange: handleCountryChange,
        className: `ship-to-country ${countryInvalid ? "invalid-country" : ""}`,
        placeholder: i18n$1["sctnh.header_shipto_select_empty"] || "Enter keyword to search.",
        options: countryDataSource,
        onMenuOpen: () => {
          onMenuStateChange == null ? void 0 : onMenuStateChange(true);
        },
        onMenuClose: () => {
          setTimeout(() => {
            onMenuStateChange == null ? void 0 : onMenuStateChange(false);
          }, 100);
        }
      }
    ), countryInvalid && /* @__PURE__ */ React.createElement(
      "span",
      {
        className: "ship-to-invalid-span",
        style: { marginTop: "14px", display: "block", marginBottom: "-7px" }
      },
      i18n$1["sctnh.header_shipto_country_empty"] || "Please select a country"
    ), /* @__PURE__ */ React.createElement("div", { id: "ship-to-popup", ref: popupRef }), /* @__PURE__ */ React.createElement(
      Input$2,
      {
        value: zip,
        country,
        onChange: handleZipChange,
        isInvalid,
        setIsInvalid,
        className: "ship-to-zip",
        i18n: i18n$1
      }
    ), /* @__PURE__ */ React.createElement("div", { className: "crated-header-ship-to-action-main" }, /* @__PURE__ */ React.createElement("button", { "data-role": "save", onClick: onSave }, i18n$1.Save)));
  }
  exports2.ShipTo = ShipTo;
  Object.defineProperty(exports2, Symbol.toStringTag, { value: "Module" });
});
