(function(global, factory) {
  typeof exports === "object" && typeof module !== "undefined" ? factory(exports, require("react")) : typeof define === "function" && define.amd ? define(["exports", "react"], factory) : (global = typeof globalThis !== "undefined" ? globalThis : global || self, factory(global.ImHeaderNotification = {}, global.React));
})(this, function(exports2, React) {
  "use strict";
  const SVG_MAP = {
    message: /* @__PURE__ */ React.createElement(
      "svg",
      {
        preserveAspectRatio: "none",
        viewBox: "0 0 1024 1024",
        width: "24",
        height: "24",
        xmlns: "http://www.w3.org/2000/svg"
      },
      /* @__PURE__ */ React.createElement("path", { d: "M853.333333 170.666667a73.142857 73.142857 0 0 1 73.142857 73.142857v487.619047a73.142857 73.142857 0 0 1-73.142857 73.142858H473.526857l-167.594667 109.83619A24.380952 24.380952 0 0 1 268.190476 894.000762V804.571429H170.666667a73.142857 73.142857 0 0 1-73.142857-73.142858V243.809524a73.142857 73.142857 0 0 1 73.142857-73.142857h682.666666z m0 73.142857H170.666667v487.619047h170.666666v72.338286L451.705905 731.428571H853.333333V243.809524zM543.207619 487.619048v73.142857H341.333333v-73.142857h201.874286zM682.666667 341.333333v73.142857H341.333333v-73.142857h341.333334z" })
    )
  };
  /*! js-cookie v3.0.5 | MIT */
  function assign(target) {
    for (var i = 1; i < arguments.length; i++) {
      var source = arguments[i];
      for (var key2 in source) {
        target[key2] = source[key2];
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
  function getDefaultExportFromCjs(x) {
    return x && x.__esModule && Object.prototype.hasOwnProperty.call(x, "default") ? x["default"] : x;
  }
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
  const ONETALK_DOMAIN = transferDomain_1("onetalk.alibaba.com");
  const MESSAGE_DOMAIN = transferDomain_1("message.alibaba.com");
  const PASSPORT_DOMAIN = transferDomain_1("passport.alibaba.com");
  const SELLER_MESSENGER_URL = `https://${ONETALK_DOMAIN}/message/weblitePWA.htm`;
  const BUYER_MESSENGER_URL = `https://${MESSAGE_DOMAIN}/message/messenger.htm`;
  const SELLER_INQUIRY_URL = `https://${MESSAGE_DOMAIN}/message/default.htm`;
  const SELLER_GGS_MESSENGER_URL = `https://${ONETALK_DOMAIN}/message/weblitePWA.htm?isGray=1&from=menu&hideMenu=1`;
  const BUYER_OFFICIAL_LOGIN_ID = "us1575531697lrni";
  const goldlog = function(data) {
    const content = `ext=${encodeURIComponent(`${data}&host=header`)}`;
    if (window.goldlog && window.goldlog.record) {
      window.goldlog.record("/sc.ma.im", "CLK", content, "GET");
    } else {
      const q = window.goldlog_queue || (window.goldlog_queue = []);
      q.push({
        action: "goldlog.record",
        arguments: ["/sc.ma.im", "CLK", content, "GET"]
      });
    }
  };
  function getHashCode(str) {
    let hashcode = 0;
    if (!str) return hashcode;
    for (let i = 0; i < str.length; i++) {
      hashcode = hashcode * 31 + str.charCodeAt(i);
      hashcode &= 4294967295;
    }
    return hashcode;
  }
  function getAvatarBackground(name) {
    const avatarBackgroundList = [
      "#50E3C2",
      "#FE5D59",
      "#FF9A59",
      "#FFDD59",
      "#59DBFF",
      "#5966FF",
      "#59ABFD",
      "#FE5977",
      "#5A8EFF",
      "#A559FF",
      "#50E3C2",
      "#D84C4C"
    ];
    return avatarBackgroundList[Math.abs(getHashCode(name) % 12)];
  }
  function formatNumber(num) {
    return num < 10 ? `0${num}` : num;
  }
  function timeSince(date) {
    if (typeof date !== "object") {
      date = new Date(date);
    }
    let seconds = Math.floor((/* @__PURE__ */ new Date() - date) / 1e3);
    const dateStr = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
    if (seconds > 60 * 60 * 24) {
      return dateStr;
    }
    const d = /* @__PURE__ */ new Date();
    const diff = (d.getTime() - new Date(d.getFullYear(), d.getMonth(), d.getDate()).getTime()) / 1e3;
    seconds -= diff;
    const interval = Math.ceil(seconds / 86400);
    const hour = formatNumber(date.getHours());
    const minute = formatNumber(date.getMinutes());
    const tt = `${hour}:${minute}`;
    return interval === 1 ? dateStr : `${tt}`;
  }
  function decodeHTML(str) {
    if (typeof str !== "string") {
      return str;
    }
    str = str.replace(/&lt;|&#60;/g, "<");
    str = str.replace(/&gt;|&#62;/g, ">");
    str = str.replace(/&apos;|&#39;/g, "'");
    str = str.replace(/&quot;|&#34;/g, '"');
    str = str.replace(/&amp;|&#38;/g, "&");
    return str;
  }
  const getCtoken = () => {
    let json = {};
    try {
      json = search2Json(api.get("xman_us_t") || "") || {};
    } catch (error) {
    }
    return json.ctoken || api.get("ctoken");
  };
  const search2Json = (searchStr) => {
    const arrayReg = /\[((\d+)(,\d+)*)?\]/;
    if (!searchStr) {
      return;
    }
    const paramItems = searchStr.split("&");
    const params = [];
    params.push("{");
    for (let i = 0, { length } = paramItems; i < length; i++) {
      const map = paramItems[i].split("=");
      params.push('"');
      params.push(map[0]);
      params.push('"');
      params.push(":");
      if (!isNaN(map[1])) {
        params.push(Number(map[1]));
      } else if (arrayReg.test(map[1])) {
        params.push(map[1]);
      } else {
        params.push('"');
        params.push(map[1]);
        params.push('"');
      }
      if (i !== length - 1) {
        params.push(",");
      }
    }
    params.push("}");
    return JSON.parse(params.join(""));
  };
  function checkLogin() {
    const { cookie } = document;
    return cookie && cookie.indexOf("sign=y") !== -1;
  }
  function getMemberType() {
    try {
      const xman_us_f = document.cookie.match(new RegExp("(^|;\\s*)xman_us_f=([^;]*)"));
      if (xman_us_f == null ? void 0 : xman_us_f.length) {
        const x_user = /(x_user=.+?)([;&])/.exec(xman_us_f[0]);
        if (x_user == null ? void 0 : x_user.length) {
          const splitResult = x_user[0].split("|");
          if (splitResult == null ? void 0 : splitResult.length) {
            return splitResult[3];
          }
        }
      }
      return "";
    } catch (e) {
      console.error("==== get member type failed ====", e);
      return "";
    }
  }
  function getMessengerUrl() {
    const type = getMemberType();
    const urlMap = {
      cgs: SELLER_INQUIRY_URL,
      tp: SELLER_GGS_MESSENGER_URL,
      ifm: BUYER_MESSENGER_URL,
      cnfm: SELLER_MESSENGER_URL
    };
    return urlMap[type] || BUYER_MESSENGER_URL;
  }
  function getBuyerLocale() {
    try {
      const matchResult = /(sc_b_locale=*.+?)[&]/.exec(document.cookie);
      let locale2 = matchResult && matchResult[1] && matchResult[1].slice(12) || "";
      locale2 = locale2.split("_");
      return {
        lang: locale2[0] || "en",
        country: locale2[1] || "US"
      };
    } catch (e) {
      console.error("==== get locale failed ====", e);
      goldlog(`getLocaleFail&msg=${e == null ? void 0 : e.message}`);
      return {
        lang: "en",
        country: "US"
      };
    }
  }
  var enUs = {
    "messenger.list.content.audio": "Voice",
    "messenger.imHeader.toLogin": "Sign in",
    "messenger.list.content.company": "Company",
    "messenger.list.content.file": "File",
    "messenger.reverseTip": "User recalled a message.",
    "messenger.list.content.businessCard": "Business card",
    "messenger.list.content.behavior": "Card",
    "messenger.list.content.message.2129": "Chatting with suppliers? Keep your purchases safe and hassle-free.",
    "messenger.list.content.message": "Message",
    "messenger.list.content.message.2128": "3 tips to keep your orders protected ",
    "messenger.list.content.message.9420": "Your order is ready.",
    "messenger.list.content.message.2146": "Be First to Try Our AI Store Agent — Exclusive Free Credits Inside ",
    "messenger.imHeader.noData": "Go to Messenger for more",
    "messenger.imHeader.message": "Messages",
    "messenger.list.content.message.2134": "Potential risk warning: Avoid chatting or transacting outside Alibaba.com",
    "messenger.list.content.video": "Video",
    "messenger.list.content.aiSummary": "Summary",
    "messenger.imHeader.viewmore": "View more",
    "messenger.list.content.ta": "Order",
    "messenger.list.content.image": "Image",
    "messenger.list.content.quotation": "Quotation",
    "messenger.list.content.tradeAssurance": "Order",
    "messenger.list.content.message.2125": "AI Mode has completed your task. Follow up now.",
    "messenger.list.content.message.2127": "Follow up on the quotation progress with AI Mode",
    "messenger.youReverseTip": "You've recalled a message.",
    "messenger.imHeader.LoginTip": "Sign in to view more",
    "messenger.list.content.text": "Message",
    "messenger.list.content.message.9421": "Your order is ready.",
    "messenger.list.content.product": "Product",
    "messenger.list.content.message.2124": "AI Mode quotation"
  };
  var jaJp = {
    "messenger.list.content.message.2125": "AI モードがタスクを完了しました。今すぐ追跡し、対応してください。",
    "messenger.imHeader.viewmore": "さらに表示",
    "messenger.list.content.message.2134": "潜在的なリスクに関する警告：Alibaba.com 外部でのチャットや取引は避けてください",
    "messenger.imHeader.noData": "メッセンジャーにアクセスしてその他のメッセージを見る",
    "messenger.list.content.ta": "注文",
    "messenger.list.content.message.9420": "ご注文の準備が整いました。",
    "messenger.list.content.aiSummary": "要約",
    "messenger.list.content.video": "動画",
    "messenger.list.content.tradeAssurance": "注文",
    "messenger.list.content.message.2127": "AI モードで見積もりの進捗を追跡し、対応",
    "messenger.imHeader.message": "メッセージ",
    "messenger.list.content.message.2128": "ご注文を保護するためのヒントは 3 つ",
    "messenger.imHeader.LoginTip": "サインインして詳細を表示",
    "messenger.list.content.text": "メッセージ",
    "messenger.list.content.file": "ファイル",
    "messenger.imHeader.toLogin": "サインイン",
    "messenger.list.content.company": "会社",
    "messenger.list.content.message": "メッセージ",
    "messenger.list.content.message.2129": "サプライヤーとチャット中ですか？購入を安全に手間なく保護します。",
    "messenger.list.content.image": "画像",
    "messenger.list.content.message.2124": "AI モードによる見積もり",
    "messenger.list.content.message.9421": "ご注文の準備が整いました。",
    "messenger.list.content.product": "製品",
    "messenger.list.content.behavior": "カード",
    "messenger.list.content.audio": "ボイス",
    "messenger.list.content.businessCard": "名刺",
    "messenger.reverseTip": "ユーザーがメッセージを元に戻しました。",
    "messenger.youReverseTip": "メッセージを元に戻しました。"
  };
  var zhCn = {
    "messenger.youReverseTip": "你撤回了一条消息",
    "messenger.list.content.message.2146": "抢先体验我们的 AI 店铺助手 — 内含独家免费额度 ",
    "messenger.list.content.ta": "订单",
    "messenger.list.content.video": "视频",
    "messenger.list.content.tradeAssurance": "订单",
    "messenger.list.content.message.9421": "订单起草完成。",
    "messenger.list.content.message": "文本",
    "messenger.list.content.product": "商品",
    "messenger.list.content.message.2134": "风险提醒：切勿在 Alibaba.com 平台外沟通或交易",
    "messenger.list.content.company": "公司",
    "messenger.imHeader.toLogin": "登录",
    "messenger.list.content.message.2125": "AI Mode完成了您的任务，请及时跟进。",
    "messenger.list.content.aiSummary": "摘要",
    "messenger.list.content.audio": "语音",
    "messenger.list.content.text": "文本",
    "messenger.list.content.message.9420": "订单起草完成。",
    "messenger.list.content.businessCard": "名片",
    "messenger.imHeader.viewmore": "查看更多",
    "messenger.list.content.file": "文件",
    "messenger.list.content.quotation": "报价",
    "messenger.list.content.message.2124": "AI Mode报价",
    "messenger.list.content.image": "图片",
    "messenger.imHeader.noData": "前往消息中心查看更多",
    "messenger.list.content.message.2127": "请跟进AI Mode报价进展",
    "messenger.imHeader.LoginTip": "登录查看更多",
    "messenger.list.content.message.2129": "在跟供应商沟通？如何确保您的沟通安全无忧",
    "messenger.imHeader.message": "消息",
    "messenger.reverseTip": "对方撤回了一条消息",
    "messenger.list.content.message.2128": "3个tips保护你的交易安全",
    "messenger.list.content.behavior": "卡片"
  };
  var hiIn = {
    "messenger.list.content.file": "फ़ाइल",
    "messenger.list.content.quotation": "कोटेशन",
    "messenger.list.content.message.2124": "AI मोड कोटेशन",
    "messenger.youReverseTip": "आपने किसी संदेश को याद किया.",
    "messenger.imHeader.toLogin": "साइन इन करें",
    "messenger.list.content.message.2125": "AI मोड ने आपका टास्क पूरा किया है. अभी फ़ॉलो अप लें.",
    "messenger.list.content.image": "छवि",
    "messenger.list.content.message.2134": "संभावित जोखिम की चेतावनी: Alibaba.com से बाहर चैट या लेनदेन करने से बचें",
    "messenger.list.content.message.2127": "AI मोड के साथ कोटेशन की प्रगति के बारे में फ़ॉलो अप लें",
    "messenger.list.content.tradeAssurance": "ऑर्डर",
    "messenger.imHeader.LoginTip": "अधिक देखने के लिए साइन इन करें",
    "messenger.list.content.audio": "आवाज़",
    "messenger.list.content.message.9420": "आपका ऑर्डर तैयार है.",
    "messenger.imHeader.noData": "अधिक के लिए मैसेंजर पर जाएं",
    "messenger.list.content.behavior": "कार्ड",
    "messenger.list.content.message.2129": "आपूर्तिकर्ताओं से चैट कर रहे हैं? अपनी खरीदारियों को सुरक्षित और बिना परेशानी वाला रखें.",
    "messenger.list.content.message.2128": "अपने ऑर्डर को सुरक्षित रखने के लिए 3 टिप्स",
    "messenger.imHeader.message": "संदेश",
    "messenger.list.content.businessCard": "बिज़नेस कार्ड",
    "messenger.list.content.aiSummary": "सारांश",
    "messenger.list.content.video": "वीडियो",
    "messenger.list.content.company": "कंपनी",
    "messenger.list.content.message": "संदेश",
    "messenger.reverseTip": "उपयोगकर्ता ने किसी संदेश को याद किया.",
    "messenger.list.content.product": "उत्पाद",
    "messenger.imHeader.viewmore": "और देखें",
    "messenger.list.content.message.9421": "आपका ऑर्डर तैयार है.",
    "messenger.list.content.ta": "ऑर्डर",
    "messenger.list.content.text": "संदेश"
  };
  var trTr = {
    "messenger.list.content.image": "Görsel",
    "messenger.list.content.video": "Video",
    "messenger.list.content.aiSummary": "Özet",
    "messenger.list.content.message.2124": "AI Modu fiyat teklifi",
    "messenger.imHeader.viewmore": "Daha fazlası",
    "messenger.list.content.behavior": "Kart",
    "messenger.list.content.message.9421": "Siparişiniz hazır.",
    "messenger.list.content.message.2128": "ใหม่ที่ Alibaba.com? เรียนรู้เกี่ยวกับบริการและการคุ้มครองของเรา",
    "messenger.list.content.text": "Mesaj",
    "messenger.list.content.ta": "Sipariş",
    "messenger.imHeader.noData": "Daha fazlası için Messenger'a gidin",
    "messenger.list.content.file": "Dosya",
    "messenger.youReverseTip": "Bir mesajı geri çağırdınız.",
    "messenger.list.content.product": "Ürün",
    "messenger.list.content.company": "Şirket",
    "messenger.imHeader.toLogin": "Giriş Yap",
    "messenger.list.content.message.9420": "Siparişiniz hazır.",
    "messenger.imHeader.message": "Mesajlar",
    "messenger.list.content.message.2134": "Potansiyel risk uyarısı: Alibaba.com dışında sohbet etmekten veya işlem yapmaktan kaçının",
    "messenger.list.content.businessCard": "Kartvizit",
    "messenger.reverseTip": "Kullanıcı bir mesajı geri çağırdı.",
    "messenger.list.content.tradeAssurance": "Sipariş",
    "messenger.list.content.audio": "Ses",
    "messenger.imHeader.LoginTip": "Daha fazlasını görüntülemek için oturum açın",
    "messenger.list.content.message": "Mesaj",
    "messenger.list.content.message.2129": "กำลังพูดคุยกับซัพพลายเออร์ใช่ไหม? ทำให้การสั่งซื้อของคุณปลอดภัยและไม่ยุ่งยาก"
  };
  var koKr = {
    "messenger.imHeader.viewmore": "더 보기",
    "messenger.imHeader.message": "메시지",
    "messenger.list.content.message.2128": "주문 보호를 유지하기 위한 3가지 팁 ",
    "messenger.list.content.message.2127": "AI 모드로 견적 진행 상황에 대한 후속 조치를 하세요",
    "messenger.list.content.video": "동영상",
    "messenger.list.content.tradeAssurance": "주문",
    "messenger.list.content.aiSummary": "요약",
    "messenger.imHeader.LoginTip": "더 보려면 로그인",
    "messenger.list.content.message.9420": "주문이 준비되었습니다.",
    "messenger.list.content.text": "메시지",
    "messenger.list.content.message.2125": "AI 모드가 작업을 완료했습니다. 지금 후속 조치를 하세요.",
    "messenger.list.content.audio": "음성",
    "messenger.list.content.ta": "주문",
    "messenger.list.content.message.2124": "AI 모드 견적",
    "messenger.list.content.message.9421": "주문이 준비되었습니다.",
    "messenger.imHeader.toLogin": "로그인",
    "messenger.list.content.product": "제품",
    "messenger.list.content.image": "이미지",
    "messenger.youReverseTip": "메시지를 회수했습니다.",
    "messenger.list.content.behavior": "카드",
    "messenger.list.content.company": "회사",
    "messenger.list.content.file": "파일",
    "messenger.list.content.message.2134": "잠재적 위험 경고: Alibaba.com 외부에서 채팅하거나 거래를 진행하지 마세요",
    "messenger.imHeader.noData": "메신저로 이동하여 더 보기",
    "messenger.list.content.message": "메시지",
    "messenger.list.content.message.2129": "공급업체와 채팅 중이신가요? 구매를 안전하고 번거로움 없이 유지하세요.",
    "messenger.list.content.quotation": "견적",
    "messenger.list.content.businessCard": "명함",
    "messenger.reverseTip": "사용자가 메시지를 회수했습니다."
  };
  var frFr = {
    "messenger.list.content.product": "Produit",
    "messenger.list.content.message.2129": "Vous discutez avec des fournisseurs ? Effectuez vos achats en toute sécurité et sans tracas.",
    "messenger.list.content.quotation": "Devis",
    "messenger.imHeader.message": "Messages",
    "messenger.imHeader.noData": "Accédez à Messenger pour plus de messages",
    "messenger.youReverseTip": "Vous avez rappelé un message.",
    "messenger.list.content.message.2125": "Le Mode IA a terminé votre tâche. Effectuez maintenant le suivi.",
    "messenger.imHeader.LoginTip": "Connectez-vous pour voir plus",
    "messenger.reverseTip": "L’utilisateur a rappelé un message.",
    "messenger.list.content.behavior": "Carte",
    "messenger.list.content.ta": "Commande",
    "messenger.list.content.image": "Image",
    "messenger.imHeader.viewmore": "En savoir plus",
    "messenger.list.content.message.2134": "Avertissement sur les risques potentiels : évitez de discuter ou d'effectuer des transactions en dehors d'Alibaba.com",
    "messenger.list.content.aiSummary": "Résumé",
    "messenger.list.content.businessCard": "Carte de visite",
    "messenger.list.content.video": "Vidéo",
    "messenger.list.content.tradeAssurance": "Commande",
    "messenger.list.content.message.9421": " Votre commande est prête.",
    "messenger.list.content.message.2128": "3 conseils pour protéger vos commandes ",
    "messenger.list.content.message": "Message",
    "messenger.list.content.audio": "Voix",
    "messenger.list.content.company": "Société",
    "messenger.list.content.message.2124": "Devis en Mode IA",
    "messenger.list.content.message.2127": "Effectuez le suivi de l'avancement du devis avec le Mode IA",
    "messenger.list.content.file": "Fichier",
    "messenger.imHeader.toLogin": "Se connecter",
    "messenger.list.content.message.9420": " Votre commande est prête.",
    "messenger.list.content.text": "Message"
  };
  var esEs = {
    "messenger.youReverseTip": "Has retirado un mensaje.",
    "messenger.list.content.video": "Vídeo",
    "messenger.list.content.tradeAssurance": "Pedido",
    "messenger.list.content.aiSummary": "Resumen",
    "messenger.list.content.ta": "Pedido",
    "messenger.list.content.product": "Producto",
    "messenger.imHeader.viewmore": "Ver más",
    "messenger.list.content.image": "Imagen",
    "messenger.imHeader.LoginTip": "Inicia sesión para ver más",
    "messenger.list.content.message.2124": "Cotización con Modo IA",
    "messenger.list.content.behavior": "Tarjeta",
    "messenger.list.content.message.2125": "El Modo IA completó tu tarea. Haz seguimiento ahora.",
    "messenger.list.content.quotation": "Cotización",
    "messenger.list.content.message.2128": "3 tips para mantener tus pedidos protegidos ",
    "messenger.list.content.businessCard": "Tarjeta de presentación",
    "messenger.imHeader.message": "Mensajes",
    "messenger.list.content.message.9421": "Tu pedido está listo.",
    "messenger.list.content.message": "Mensaje ",
    "messenger.list.content.message.2127": "Haz seguimiento del progreso de la cotización con el Modo IA",
    "messenger.list.content.message.2134": "Advertencia de posibles riesgos: evita chatear o realizar transacciones fuera de Alibaba.com",
    "messenger.list.content.file": "Archivo",
    "messenger.imHeader.noData": "Ir a Messenger para ver más",
    "messenger.list.content.message.2129": "¿Chateas con proveedores? Mantén tus compras seguras y sin complicaciones.",
    "messenger.imHeader.toLogin": "Iniciar sesión",
    "messenger.list.content.audio": "Voz",
    "messenger.reverseTip": "El usuario retiró un mensaje.",
    "messenger.list.content.message.9420": "Tu pedido está listo.",
    "messenger.list.content.text": "Mensaje",
    "messenger.list.content.company": "Empresa"
  };
  var inId = {
    "messenger.list.content.message.9420": "Pesanan Anda sudah siap.",
    "messenger.list.content.company": "Perusahaan",
    "messenger.list.content.message.2127": "Lakukan tindak lanjut pada kemajuan kuotasi dengan Mode AI",
    "messenger.list.content.message.2124": "Kuotasi Mode AI",
    "messenger.list.content.message.2128": "3 tip untuk menjaga pesanan Anda tetap terlindungi ",
    "messenger.list.content.message.9421": "Pesanan Anda sudah siap.",
    "messenger.list.content.file": "File",
    "messenger.list.content.tradeAssurance": "Pesan",
    "messenger.list.content.product": "Produk",
    "messenger.list.content.message": "Pesan",
    "messenger.list.content.ta": "Pesan",
    "messenger.imHeader.viewmore": "Lihat Lainnya",
    "messenger.list.content.businessCard": "Kartu bisnis",
    "messenger.imHeader.toLogin": "Masuk",
    "messenger.list.content.audio": "Suara",
    "messenger.list.content.video": "Video",
    "messenger.youReverseTip": "Anda telah menarik kembali pesan.",
    "messenger.list.content.aiSummary": "Ringkasan",
    "messenger.imHeader.message": "Pesan",
    "messenger.list.content.behavior": "Kartu",
    "messenger.imHeader.noData": "Buka Messenger untuk selengkapnya",
    "messenger.list.content.message.2125": "Mode AI telah menyelesaikan tugas Anda. Lakukan tindak lanjut sekarang.",
    "messenger.list.content.image": "Gambar",
    "messenger.reverseTip": "Pengguna telah menarik kembali pesan.",
    "messenger.list.content.message.2134": "Peringatan risiko potensial: Hindari obrolan atau transaksi di luar Alibaba.com",
    "messenger.list.content.message.2129": "Mengobrol dengan supplier? Buat pembelian Anda tetap aman dan mudah.",
    "messenger.imHeader.LoginTip": "Masuk untuk lihat selengkapnya",
    "messenger.list.content.text": "Pesan",
    "messenger.list.content.quotation": "Penawaran"
  };
  var arSa = {
    "messenger.imHeader.LoginTip": "سجِّل دخولك لعرض المزيد",
    "messenger.list.content.message.2124": "عرض أسعار بوضع AI",
    "messenger.list.content.file": "ملف",
    "messenger.list.content.quotation": "عرض أسعار",
    "messenger.list.content.message.9420": "طلبك جاهز.",
    "messenger.list.content.message.2129": "هل تدردش مع المورِّدين؟ حافظ على أمان مشترياتك وسيرها بلا متاعب.",
    "messenger.imHeader.noData": "انتقل إلى تطبيق المراسلة للمزيد",
    "messenger.list.content.company": "الشركة",
    "messenger.list.content.text": "رسالة",
    "messenger.youReverseTip": "لقد استرددت رسالة.",
    "messenger.list.content.image": "صورة",
    "messenger.list.content.product": "منتج",
    "messenger.reverseTip": "استرد المستخدم رسالة.",
    "messenger.list.content.message": "رسالة",
    "messenger.list.content.ta": "الطلب",
    "messenger.list.content.tradeAssurance": "الطلب",
    "messenger.imHeader.viewmore": "عرض المزيد",
    "messenger.list.content.message.9421": "طلبك جاهز.",
    "messenger.list.content.businessCard": "بطاقة الأعمال",
    "messenger.imHeader.message": "الرسائل",
    "messenger.list.content.audio": "صوت",
    "messenger.imHeader.toLogin": "تسجيل الدخول",
    "messenger.list.content.message.2128": "3 نصائح للحفاظ على طلباتك محمية",
    "messenger.list.content.message.2127": "تابِع سير عرض الأسعار باستخدام وضع AI",
    "messenger.list.content.video": "فيديو",
    "messenger.list.content.aiSummary": "ملخص",
    "messenger.list.content.behavior": "بطاقة",
    "messenger.list.content.message.2134": "تحذير من مخاطر محتملة: تجنب الدردشة أو إجراء معاملات خارج Alibaba.com",
    "messenger.list.content.message.2125": "لقد أكمل وضع AI مهمتك. يمكنك المتابعة الآن."
  };
  var viVn = {
    "messenger.list.content.businessCard": "Danh thiếp",
    "messenger.imHeader.message": "Tin nhắn",
    "messenger.list.content.product": "Sản phẩm",
    "messenger.list.content.message.2125": "Chế độ AI đã hoàn thành tác vụ của bạn. Hãy theo sát ngay.",
    "messenger.list.content.company": "Công ty",
    "messenger.list.content.file": "Tệp tin",
    "messenger.list.content.message.9420": "Đơn hàng của bạn đã sẵn sàng.",
    "messenger.list.content.message": "Tin nhắn",
    "messenger.list.content.text": "Tin nhắn",
    "messenger.list.content.image": "Hình ảnh",
    "messenger.list.content.audio": "Giọng nói",
    "messenger.youReverseTip": "Bạn đã thu hồi tin nhắn.",
    "messenger.reverseTip": "Người dùng đã thu hồi tin nhắn.",
    "messenger.list.content.message.2134": "Cảnh báo nguy cơ tiềm ẩn: Tránh trò chuyện hoặc giao dịch bên ngoài Alibaba.com",
    "messenger.list.content.aiSummary": "Tóm tắt",
    "messenger.list.content.video": "Video",
    "messenger.list.content.message.2124": "Báo giá từ Chế độ AI",
    "messenger.list.content.quotation": "Báo giá",
    "messenger.list.content.tradeAssurance": "Đặt hàng",
    "messenger.list.content.ta": "Đặt hàng",
    "messenger.list.content.message.9421": "Đơn hàng của bạn đã sẵn sàng.",
    "messenger.list.content.message.2128": "3 mẹo để đảm bảo đơn hàng của bạn luôn được bảo vệ:",
    "messenger.imHeader.viewmore": "Xem thêm",
    "messenger.list.content.behavior": "Thẻ",
    "messenger.imHeader.toLogin": "Đăng Nhập",
    "messenger.list.content.message.2129": "Bạn đang trò chuyện với nhà cung cấp? Đảm bảo đơn mua của bạn luôn an toàn và không phiền toái.",
    "messenger.imHeader.noData": "Truy cập Messenger để trò chuyện thêm",
    "messenger.list.content.message.2127": "Theo sát tiến độ báo giá cùng Chế độ AI",
    "messenger.imHeader.LoginTip": "Đăng nhập để xem thêm"
  };
  var ptPt = {
    "messenger.list.content.message.2124": "Cotação com Modo IA",
    "messenger.imHeader.message": "Mensagens",
    "messenger.list.content.message.2127": "Acompanhe o progresso da cotação com o Modo IA",
    "messenger.list.content.tradeAssurance": "Pedido",
    "messenger.list.content.audio": "Voz",
    "messenger.list.content.text": "Mensagem",
    "messenger.list.content.company": "Empresa",
    "messenger.list.content.ta": "Pedido",
    "messenger.imHeader.LoginTip": "Entre para ver mais",
    "messenger.list.content.aiSummary": "Resumo",
    "messenger.list.content.quotation": "Cotação",
    "messenger.list.content.message.9421": "Seu pedido está pendente de finalização.",
    "messenger.list.content.businessCard": "Cartão de visita",
    "messenger.imHeader.noData": "Acesse o Messenger para mais informações",
    "messenger.list.content.file": "Arquivo",
    "messenger.reverseTip": "O usuário cancelou uma mensagem.",
    "messenger.list.content.message.9420": "Seu pedido está pendente de finalização.",
    "messenger.list.content.message.2134": "Aviso de risco em potencial: evite conversar ou negociar fora do Alibaba.com",
    "messenger.list.content.image": "Imagem",
    "messenger.imHeader.viewmore": "Ver Mais",
    "messenger.list.content.behavior": "Cartão",
    "messenger.list.content.message.2128": "3 dicas para manter seus pedidos protegidos",
    "messenger.youReverseTip": "Você cancelou uma mensagem.",
    "messenger.list.content.message.2125": "O Modo IA concluiu sua tarefa. Acompanhe o andamento.",
    "messenger.imHeader.toLogin": "Entrar",
    "messenger.list.content.video": "Vídeo",
    "messenger.list.content.message": "Mensagem",
    "messenger.list.content.product": "Produto",
    "messenger.list.content.message.2129": "Conversando com fornecedores? Mantenha suas compras seguras e sem complicações."
  };
  var deDe = {
    "messenger.list.content.message.2125": "Der KI-Modus hat Ihre Anfrage abgeschlossen. Jetzt nachfassen.",
    "messenger.list.content.message.9421": "Ihre Bestellung ist fertig.",
    "messenger.list.content.message": "Nachricht",
    "messenger.list.content.tradeAssurance": "Bestellung",
    "messenger.list.content.audio": "Sprache",
    "messenger.list.content.message.2124": "KI-Modus-Angebot",
    "messenger.list.content.message.9420": "Ihre Bestellung ist fertig.",
    "messenger.list.content.message.2134": "Warnung vor potenziellen Risiken: nicht außerhalb von Alibaba.com chatten oder Transaktionen durchführen",
    "messenger.list.content.businessCard": "Visitenkarte",
    "messenger.list.content.image": "Bild",
    "messenger.reverseTip": "Benutzer hat eine Nachricht zurückgerufen.",
    "messenger.list.content.text": "Nachricht",
    "messenger.list.content.message.2128": "3 Tipps, um Ihre Bestellungen zu schützen",
    "messenger.imHeader.toLogin": "Anmelden",
    "messenger.list.content.product": "Produkt",
    "messenger.list.content.behavior": "Karte",
    "messenger.youReverseTip": "Sie haben eine Nachricht zurückgerufen.",
    "messenger.list.content.company": "Unternehmen",
    "messenger.list.content.message.2127": "Angebotsfortschritt mit dem KI-Modus nachfassen",
    "messenger.imHeader.LoginTip": "Anmelden, um mehr anzuzeigen",
    "messenger.list.content.quotation": "Angebot",
    "messenger.list.content.file": "Datei",
    "messenger.imHeader.viewmore": "Mehr anzeigen",
    "messenger.list.content.ta": "Bestellung",
    "messenger.imHeader.noData": "Weitere Details finden Sie im Messenger",
    "messenger.list.content.message.2129": "Chatten Sie mit Lieferanten? Halten Sie Ihre Einkäufe sicher und problemlos.",
    "messenger.imHeader.message": "Nachrichten",
    "messenger.list.content.aiSummary": "Zusammenfassung",
    "messenger.list.content.video": "Video"
  };
  var thTh = {
    "messenger.list.content.image": "รูปภาพ",
    "messenger.list.content.message.2128": "3 เคล็ดลับในการทำให้คำสั่งซื้อของคุณได้รับการคุ้มครอง",
    "messenger.list.content.tradeAssurance": "สั่งซื้อ",
    "messenger.list.content.message": "ข้อความ",
    "messenger.list.content.behavior": "การ์ด",
    "messenger.list.content.message.9420": "คำสั่งซื้อของคุณพร้อมแล้ว",
    "messenger.list.content.aiSummary": "สรุป",
    "messenger.list.content.video": "วิดีโอ",
    "messenger.list.content.businessCard": "นามบัตร",
    "messenger.list.content.message.2124": "การเสนอราคาโหมด AI",
    "messenger.list.content.company": "บริษัท",
    "messenger.list.content.message.2129": "กำลังพูดคุยกับซัพพลายเออร์ใช่ไหม? ทำให้การสั่งซื้อของคุณปลอดภัยและไม่ยุ่งยาก",
    "messenger.reverseTip": "ผู้ใช้เรียกคืนข้อความ",
    "messenger.list.content.text": "ข้อความ",
    "messenger.list.content.message.9421": "คำสั่งซื้อของคุณพร้อมแล้ว",
    "messenger.imHeader.LoginTip": "ลงชื่อเข้าระบบเพื่อดูเพิ่มเติม",
    "messenger.imHeader.toLogin": "เข้าสู่ระบบ",
    "messenger.list.content.product": "ผลิตภัณฑ์",
    "messenger.imHeader.viewmore": "ดูเพิ่มเติม",
    "messenger.list.content.quotation": "ใบเสนอราคา",
    "messenger.list.content.file": "ไฟล์",
    "messenger.list.content.ta": "สั่งซื้อ",
    "messenger.list.content.message.2125": "โหมด AI ได้ทำภารกิจของคุณสำเร็จแล้ว ติดตามได้เลย ",
    "messenger.list.content.audio": "เสียง",
    "messenger.list.content.message.2134": "คำเตือนความเสี่ยงที่อาจเกิดขึ้น : หลีกเลี่ยงการสนทนาหรือทำธุรกรรมนอก Alibaba.com",
    "messenger.imHeader.noData": "ไปที่ Messenger เพื่อดูข้อความอื่น",
    "messenger.youReverseTip": "คุณได้เรียกคืนข้อความ",
    "messenger.imHeader.message": "ข้อความ",
    "messenger.list.content.message.2127": "ติดตามความคืบหน้าของใบเสนอราคาด้วยโหมด AI"
  };
  var itIt = {
    "messenger.list.content.tradeAssurance": "Ordine",
    "messenger.imHeader.message": "Messaggi",
    "messenger.list.content.aiSummary": "Riepilogo",
    "messenger.list.content.video": "Video",
    "messenger.list.content.product": "Prodotto",
    "messenger.list.content.audio": "Voce",
    "messenger.youReverseTip": "Hai richiamato un messaggio.",
    "messenger.list.content.file": "File",
    "messenger.list.content.message.2127": " Esegui il follow-up sull'avanzamento del preventivo con AI Mode",
    "messenger.list.content.message.2134": "Avviso: potenziale rischio, evita di chattare o effettuare transazioni fuori da Alibaba.com",
    "messenger.list.content.message.2129": "Chatti con i fornitori? Tieni i tuoi acquisti al sicuro e senza complicazioni.",
    "messenger.list.content.company": "Azienda",
    "messenger.list.content.message": "Messaggio",
    "messenger.imHeader.LoginTip": "Accedi per visualizzare altro",
    "messenger.list.content.message.2125": "AI Mode ha completato la tua attività. Esegui subito il follow-up.",
    "messenger.list.content.ta": "Ordina",
    "messenger.list.content.text": "Messaggio",
    "messenger.list.content.quotation": "Preventivo",
    "messenger.list.content.businessCard": "Biglietto da visita",
    "messenger.reverseTip": "L'utente ha richiamato un messaggio.",
    "messenger.list.content.image": "Immagine",
    "messenger.list.content.behavior": "Scheda",
    "messenger.imHeader.viewmore": "Vedi altro",
    "messenger.list.content.message.9421": " Il tuo ordine è pronto.",
    "messenger.imHeader.toLogin": "Iscriviti",
    "messenger.list.content.message.2124": "Preventivo AI Mode",
    "messenger.imHeader.noData": "Vai a Messenger per altri messaggi",
    "messenger.list.content.message.9420": " Il tuo ordine è pronto.",
    "messenger.list.content.message.2128": "3 consigli per proteggere i tuoi ordini"
  };
  var nlNl = {
    "messenger.list.content.behavior": "Kaart",
    "messenger.list.content.message.2127": "Volg de voortgang van de offerte met AI-modus",
    "messenger.list.content.message.9420": "Uw bestelling is gereed.",
    "messenger.list.content.ta": "Bestelling",
    "messenger.list.content.message.2128": "3 tips om uw bestellingen te beschermen",
    "messenger.imHeader.LoginTip": "Meld u aan om meer te bekijken",
    "messenger.youReverseTip": "U hebt een bericht teruggeroepen.",
    "messenger.imHeader.toLogin": "Aanmelden",
    "messenger.list.content.product": "Product",
    "messenger.list.content.businessCard": "Visitekaartje",
    "messenger.list.content.company": "Bedrijf",
    "messenger.list.content.message.2129": "Aan het chatten met leveranciers? Houd uw aankopen veilig en zorgeloos.",
    "messenger.reverseTip": "De gebruiker heeft een bericht teruggeroepen.",
    "messenger.list.content.quotation": "Offerte",
    "messenger.imHeader.message": "Berichten",
    "messenger.list.content.tradeAssurance": "Bestelling",
    "messenger.list.content.video": "Video",
    "messenger.list.content.message.2124": "Offerte van AI-modus",
    "messenger.list.content.message.2125": "AI-modus heeft uw taak voltooid. Volg deze nu op.",
    "messenger.list.content.text": "Bericht",
    "messenger.imHeader.viewmore": "Meer weergeven",
    "messenger.list.content.audio": "Stem",
    "messenger.list.content.image": "Afbeelding",
    "messenger.list.content.message": "Bericht",
    "messenger.list.content.message.9421": "Uw bestelling is gereed.",
    "messenger.list.content.aiSummary": "Samenvatting",
    "messenger.list.content.message.2134": "Waarschuwing voor mogelijk risico: vermijd chatten of transacties buiten Alibaba.com",
    "messenger.list.content.file": "Bestand",
    "messenger.imHeader.noData": "Ga naar Messenger voor meer"
  };
  var ruRu = {
    "messenger.list.content.message.2125": "Режим ИИ выполнил вашу задачу. Посмотрите.",
    "messenger.list.content.message.2127": "Посмотрите прогресс коммерческого предложения с Режимом ИИ",
    "messenger.list.content.message.2134": "Предупреждение о потенциальных рисках: избегайте общения или проведения транзакций за пределами Alibaba.com",
    "messenger.list.content.video": "Видео",
    "messenger.list.content.product": "Товар",
    "messenger.list.content.company": "Компания",
    "messenger.imHeader.LoginTip": "Войдите, чтобы увидеть больше",
    "messenger.list.content.text": "Сообщение",
    "messenger.list.content.message.9421": "Ваш заказ готов.",
    "messenger.imHeader.message": "Сообщения",
    "messenger.list.content.behavior": "Карта",
    "messenger.list.content.businessCard": "Визитная карточка",
    "messenger.list.content.quotation": "Ответ",
    "messenger.reverseTip": "Пользователь отозвал отправленное сообщение.",
    "messenger.list.content.message.2129": "Общаетесь с поставщиками? Обезопасьте свои покупки без забот.",
    "messenger.list.content.message.2128": "3 совета, как защитить ваши заказы",
    "messenger.imHeader.noData": "Чтобы узнать больше, переходите в Messenger",
    "messenger.imHeader.toLogin": "Войти",
    "messenger.list.content.image": "Изображение",
    "messenger.imHeader.viewmore": "Показать еще",
    "messenger.list.content.tradeAssurance": "Заказ",
    "messenger.list.content.aiSummary": "Сводная информация",
    "messenger.list.content.audio": "Голос",
    "messenger.youReverseTip": "Вы отозвали отправленное сообщение.",
    "messenger.list.content.message.2124": "Коммерческое предложение в режиме ИИ",
    "messenger.list.content.file": "Файл",
    "messenger.list.content.message.9420": "Ваш заказ готов.",
    "messenger.list.content.message": "Сообщение",
    "messenger.list.content.ta": "Заказ"
  };
  var iwIl = {
    "messenger.list.content.tradeAssurance": "הזמנה",
    "messenger.list.content.message.9420": "ההזמנה שלכם מוכנה.",
    "messenger.list.content.businessCard": "כרטיס ביקור",
    "messenger.list.content.file": "קובץ",
    "messenger.list.content.message": "הודעה",
    "messenger.list.content.ta": "הזמנה",
    "messenger.imHeader.viewmore": "הצגת עוד",
    "messenger.list.content.product": "מוצר",
    "messenger.list.content.message.2134": "אזהרת סיכון פוטנציאלי: חשוב לא לשוח ולא לבצע עסקאות מחוץ ל- Alibaba.com",
    "messenger.reverseTip": "המשתמש ביקש להחזיר אליו את ההודעה.",
    "messenger.imHeader.toLogin": "היכנס",
    "messenger.list.content.message.2127": "עקבו אחרי התקדמות הצעת המחיר עם מצב בינה מלאכותית",
    "messenger.list.content.quotation": "הצעת מחיר",
    "messenger.list.content.company": "חברה",
    "messenger.youReverseTip": "ההודעה אוחזרה.",
    "messenger.list.content.message.2128": "3 טיפים להגנה על ההזמנות",
    "messenger.list.content.message.2125": "מצב בינה מלאכותית השלים את המשימה שלכם. עקבו עכשיו.",
    "messenger.imHeader.message": "הודעות",
    "messenger.list.content.text": "הודעה",
    "messenger.list.content.message.2124": "הצעת מחיר של מצב בינה מלאכותית",
    "messenger.list.content.message.9421": "ההזמנה שלכם מוכנה.",
    "messenger.list.content.image": "תמונה",
    "messenger.list.content.message.2129": "משוחחים בצ'אט עם ספקים? שמרו על תהליך רכש בטוח וללא דאגות.",
    "messenger.list.content.behavior": "כרטיס",
    "messenger.list.content.audio": "קול",
    "messenger.imHeader.LoginTip": "היכנסו כדי להציג עוד",
    "messenger.list.content.aiSummary": "סיכום",
    "messenger.list.content.video": "וידאו",
    "messenger.imHeader.noData": "עברו למסנג'ר למידע נוסף"
  };
  var zhTw = {
    "messenger.list.content.image": "圖片",
    "messenger.list.content.businessCard": "名片",
    "messenger.list.content.message": "文字",
    "messenger.list.content.quotation": "報價",
    "messenger.list.content.audio": "語音",
    "messenger.list.content.text": "文字",
    "messenger.reverseTip": "對方撤回了一條消息",
    "messenger.list.content.company": "公司",
    "messenger.list.content.tradeAssurance": "訂單",
    "messenger.list.content.message.2134": "潛在風險提醒：請避免在 Alibaba.com 以外進行溝通或交易",
    "messenger.list.content.file": "文件",
    "messenger.list.content.message.9420": "您的訂單已就緒。",
    "messenger.list.content.product": "商品",
    "messenger.list.content.ta": "訂單",
    "messenger.youReverseTip": "你撤回了一條消息",
    "messenger.list.content.video": "視頻",
    "messenger.list.content.behavior": "卡片",
    "messenger.list.content.message.9421": "您的訂單已就緒。",
    "messenger.list.content.aiSummary": "摘要"
  };
  var bnIn = {
    "messenger.list.content.message.9420": "##@@@messenger.list.content.message.9420##intl-gangesweb@@@##",
    "messenger.youReverseTip": "##@@@messenger.youReverseTip##intl-gangesweb@@@##",
    "messenger.list.content.image": "##@@@messenger.list.content.image##intl-gangesweb@@@##",
    "messenger.list.content.aiSummary": "##@@@messenger.list.content.aiSummary##intl-gangesweb@@@##",
    "messenger.list.content.message.2134": "##@@@messenger.list.content.message.2134##intl-gangesweb@@@##",
    "messenger.list.content.message": "##@@@messenger.list.content.message##intl-gangesweb@@@##",
    "messenger.list.content.message.9421": "##@@@messenger.list.content.message.9421##intl-gangesweb@@@##",
    "messenger.list.content.message.2124": "##@@@messenger.list.content.message.2124##intl-gangesweb@@@##",
    "messenger.list.content.product": "##@@@messenger.list.content.product##intl-gangesweb@@@##",
    "messenger.list.content.businessCard": "##@@@messenger.list.content.businessCard##intl-gangesweb@@@##",
    "messenger.list.content.message.2125": "##@@@messenger.list.content.message.2125##intl-gangesweb@@@##",
    "messenger.list.content.message.2129": "##@@@messenger.list.content.message.2129##intl-gangesweb@@@##",
    "messenger.list.content.company": "##@@@messenger.list.content.company##intl-gangesweb@@@##",
    "messenger.list.content.message.2146": "##@@@messenger.list.content.message.2146##intl-gangesweb@@@##",
    "messenger.list.content.behavior": "##@@@messenger.list.content.behavior##intl-gangesweb@@@##",
    "messenger.list.content.message.2127": "##@@@messenger.list.content.message.2127##intl-gangesweb@@@##",
    "messenger.reverseTip": "##@@@messenger.reverseTip##intl-gangesweb@@@##",
    "messenger.list.content.message.2128": "##@@@messenger.list.content.message.2128##intl-gangesweb@@@##",
    "messenger.list.content.ta": "##@@@messenger.list.content.ta##intl-gangesweb@@@##"
  };
  var zhVn = {
    "messenger.list.content.company": "公司",
    "messenger.list.content.image": "图片",
    "messenger.list.content.text": "文本",
    "messenger.list.content.video": "视频",
    "messenger.imHeader.viewmore": "查看更多",
    "messenger.imHeader.toLogin": "登录",
    "messenger.list.content.message.2128": "3个tips保护你的交易安全",
    "messenger.list.content.message.2134": "风险提醒：切勿在 Alibaba.com 平台外沟通或交易",
    "messenger.reverseTip": "对方撤回了一条消息",
    "messenger.list.content.file": "文件",
    "messenger.imHeader.noData": "前往消息中心查看更多",
    "messenger.list.content.message": "文本",
    "messenger.list.content.behavior": "卡片",
    "messenger.list.content.audio": "语音",
    "messenger.list.content.quotation": "报价",
    "messenger.imHeader.LoginTip": "登录查看更多",
    "messenger.list.content.tradeAssurance": "订单",
    "messenger.list.content.message.2125": "AI Mode完成了您的任务，请及时跟进。",
    "messenger.imHeader.message": "消息",
    "messenger.list.content.message.2124": "AI Mode报价",
    "messenger.list.content.product": "商品",
    "messenger.list.content.businessCard": "名片",
    "messenger.list.content.message.2129": "在跟供应商沟通？如何确保您的沟通安全无忧",
    "messenger.list.content.message.2127": "请跟进AI Mode报价进展",
    "messenger.youReverseTip": "你撤回了一条消息",
    "messenger.list.content.ta": "订单",
    "messenger.list.content.aiSummary": "摘要"
  };
  var plPl = {
    "messenger.list.content.aiSummary": "Podsumowanie",
    "messenger.list.content.message.2124": "Otrzymano wycenę w trybie AI",
    "messenger.youReverseTip": "Wiadomość została wycofana.",
    "messenger.list.content.ta": "Zamówienie",
    "messenger.imHeader.viewmore": "Zobacz więcej",
    "messenger.list.content.message.2127": "Śledź postępy w wycenie z Trybem AI.",
    "messenger.imHeader.toLogin": "Zaloguj się",
    "messenger.list.content.text": "Wiadomość",
    "messenger.list.content.message.2128": "3 wskazówki, jak chronić swoje zamówienia",
    "messenger.list.content.quotation": "Wycena",
    "messenger.list.content.message": "Wiadomość",
    "messenger.imHeader.LoginTip": "Zaloguj się, aby zobaczyć więcej.",
    "messenger.imHeader.noData": "Przejdź do Messengera po więcej",
    "messenger.imHeader.message": "Wiadomości",
    "messenger.list.content.message.2129": "Czatujesz z dostawcami? Kupuj bezpiecznie i bezproblemowo.",
    "messenger.list.content.product": "Produkt",
    "messenger.list.content.tradeAssurance": "Zamówienie",
    "messenger.list.content.message.2134": "Ostrzeżenie o potencjalnym ryzyku: Unikaj czatowania lub dokonywania transakcji poza Alibaba.com.",
    "messenger.list.content.message.9420": "Twoje zamówienie jest gotowe.",
    "messenger.list.content.video": "Wideo",
    "messenger.list.content.image": "Obraz",
    "messenger.list.content.company": "Firma",
    "messenger.list.content.audio": "Głos",
    "messenger.list.content.message.9421": "Twoje zamówienie jest gotowe.",
    "messenger.list.content.behavior": "Karta",
    "messenger.reverseTip": "Użytkownik wycofał wiadomość.",
    "messenger.list.content.message.2125": "Tryb AI wykonał Twoje zadanie. Sprawdź teraz.",
    "messenger.list.content.businessCard": "Wizytówka",
    "messenger.list.content.file": "Dodaj do koszyka zapytań\nDodano do koszyka zapytań.\nProdukt jest już w koszyku zapytań.\nZobacz koszyk zapytań\nWyślij zapytanie\nWyślij\nKoszyk zapytań\nTwoje zapytanie zostało pomyślnie wysłane.\nPrzedstawiciel handlowy skontaktuje się z Państwem w ciągu 24 godzin.\nZarządzaj RFQ\nCo to jest RFQ?\nRFQ (Request for Quotation, czyli zapytanie ofertowe) to proces biznesowy, w którym firma prosi dostawcę o wycenę na zakup określonych produktów lub usług.\nUtwórz RFQ\nNazwa produktu\nIlość\nOczekiwana cena\nJednostka\nProszę podać nazwę produktu.\nProszę podać prawidłową ilość.\nTwoje zapytanie RFQ dotyczące „${productName}” zostało złożone.\nNumer zamówienia\nData zamówienia\nKwota całkowita\nStatus\nOczekuje na płatność\nW trakcie realizacji\nWysłano\nDostarczono\nAnulowano\nZobacz szczegóły zamówienia\nŚledź przesyłkę\nAdres dostawy\nAdres rozliczeniowy\nAdres dostawy jest taki sam jak adres rozliczeniowy.\nMetoda płatności\nPrzetwarzamy Państwa zamówienie ${orderId}.\nPaństwa zamówienie zostało wysłane. Numer do śledzenia przesyłki to ${trackingNumber}."
  };
  var tlPh = {
    "messenger.imHeader.noData": "Pumunta sa Messenger para sa higit pa",
    "messenger.imHeader.viewmore": "Tingnan pa",
    "messenger.list.content.product": "Produkto",
    "messenger.imHeader.message": "Mga Mensahe",
    "messenger.list.content.message": "Mensahe",
    "messenger.list.content.message.9420": "Handa na ang iyong order.",
    "messenger.list.content.behavior": "Card",
    "messenger.list.content.aiSummary": "Buod",
    "messenger.list.content.ta": "Order",
    "messenger.list.content.video": "Video",
    "messenger.list.content.businessCard": "Business card",
    "messenger.list.content.message.2127": "I-follow up ang progreso ng quotation gamit ang AI Mode",
    "messenger.list.content.message.2134": "Babala sa posibleng panganib: Iwasan ang pakikipag-chat o transaksyon sa labas ng Alibaba.com",
    "messenger.imHeader.toLogin": "Mag-sign in",
    "messenger.list.content.company": "Kumpanya",
    "messenger.list.content.image": "Larawan",
    "messenger.list.content.audio": "Boses",
    "messenger.list.content.file": "File",
    "messenger.youReverseTip": "Binawi mo ang isang mensahe.",
    "messenger.list.content.quotation": "Kotesyon",
    "messenger.list.content.tradeAssurance": "Order",
    "messenger.list.content.message.2124": "Natanggap ang quotation sa AI Mode",
    "messenger.reverseTip": "Binawi ng user ang isang mensahe.",
    "messenger.list.content.message.9421": "Handa na ang iyong order.",
    "messenger.list.content.message.2129": "Nakikipag-chat sa mga supplier? Panatilihing ligtas at walang abala ang iyong mga pinamili.",
    "messenger.list.content.text": "Mensahe",
    "messenger.list.content.message.2125": "Nakumpleto na ng AI Mode ang iyong gawain. I-follow up na.",
    "messenger.list.content.message.2128": "3 mga tip para mapanatiling protektado ang iyong mga order",
    "messenger.imHeader.LoginTip": "Mag-sign in upang tingnan pa"
  };
  var i18n = {};
  var defaultLocale = "en-us";
  i18n["en-us"] = enUs;
  i18n["ja-jp"] = jaJp;
  i18n["zh-cn"] = zhCn;
  i18n["hi-in"] = hiIn;
  i18n["tr-tr"] = trTr;
  i18n["ko-kr"] = koKr;
  i18n["fr-fr"] = frFr;
  i18n["es-es"] = esEs;
  i18n["in-id"] = inId;
  i18n["ar-sa"] = arSa;
  i18n["vi-vn"] = viVn;
  i18n["pt-pt"] = ptPt;
  i18n["de-de"] = deDe;
  i18n["th-th"] = thTh;
  i18n["it-it"] = itIt;
  i18n["nl-nl"] = nlNl;
  i18n["ru-ru"] = ruRu;
  i18n["iw-il"] = iwIl;
  i18n["zh-tw"] = zhTw;
  i18n["bn-in"] = bnIn;
  i18n["zh-vn"] = zhVn;
  i18n["pl-pl"] = plPl;
  i18n["tl-ph"] = tlPh;
  for (var locale$1 in i18n) {
    if (!i18n.hasOwnProperty(locale$1)) {
      continue;
    }
    if (locale$1 == defaultLocale) {
      continue;
    }
    for (var key in i18n[defaultLocale]) {
      if (!i18n[defaultLocale].hasOwnProperty(key)) {
        continue;
      }
      if (!i18n[locale$1].hasOwnProperty(key)) {
        i18n[locale$1][key] = i18n[defaultLocale][key];
      }
    }
  }
  i18n.appName = "intl-gangesweb";
  i18n.groupName = "im-header";
  i18n.defaultLocale = defaultLocale;
  var mcms_intlGangesweb_imHeader = i18n;
  const I18NData = /* @__PURE__ */ getDefaultExportFromCjs(mcms_intlGangesweb_imHeader);
  const locale = getBuyerLocale();
  const languageMap = {
    "iw-he": "iw-il",
    "zh-tw": "zh-cn",
    "fil-ph": "tl-ph"
  };
  const I18N = {
    get(key2) {
      var _a;
      let language = "en-us";
      if (locale) {
        language = `${locale.lang}-${locale.country}`.toLowerCase();
      }
      language = languageMap[language] || language;
      return (_a = I18NData[language]) == null ? void 0 : _a[key2];
    }
  };
  /*! @license DOMPurify 3.4.0 | (c) Cure53 and other contributors | Released under the Apache license 2.0 and Mozilla Public License 2.0 | github.com/cure53/DOMPurify/blob/3.4.0/LICENSE */
  const {
    entries,
    setPrototypeOf,
    isFrozen,
    getPrototypeOf,
    getOwnPropertyDescriptor
  } = Object;
  let {
    freeze,
    seal,
    create
  } = Object;
  let {
    apply,
    construct
  } = typeof Reflect !== "undefined" && Reflect;
  if (!freeze) {
    freeze = function freeze2(x) {
      return x;
    };
  }
  if (!seal) {
    seal = function seal2(x) {
      return x;
    };
  }
  if (!apply) {
    apply = function apply2(func, thisArg) {
      for (var _len = arguments.length, args = new Array(_len > 2 ? _len - 2 : 0), _key = 2; _key < _len; _key++) {
        args[_key - 2] = arguments[_key];
      }
      return func.apply(thisArg, args);
    };
  }
  if (!construct) {
    construct = function construct2(Func) {
      for (var _len2 = arguments.length, args = new Array(_len2 > 1 ? _len2 - 1 : 0), _key2 = 1; _key2 < _len2; _key2++) {
        args[_key2 - 1] = arguments[_key2];
      }
      return new Func(...args);
    };
  }
  const arrayForEach = unapply(Array.prototype.forEach);
  const arrayLastIndexOf = unapply(Array.prototype.lastIndexOf);
  const arrayPop = unapply(Array.prototype.pop);
  const arrayPush = unapply(Array.prototype.push);
  const arraySplice = unapply(Array.prototype.splice);
  const stringToLowerCase = unapply(String.prototype.toLowerCase);
  const stringToString = unapply(String.prototype.toString);
  const stringMatch = unapply(String.prototype.match);
  const stringReplace = unapply(String.prototype.replace);
  const stringIndexOf = unapply(String.prototype.indexOf);
  const stringTrim = unapply(String.prototype.trim);
  const objectHasOwnProperty = unapply(Object.prototype.hasOwnProperty);
  const regExpTest = unapply(RegExp.prototype.test);
  const typeErrorCreate = unconstruct(TypeError);
  function unapply(func) {
    return function(thisArg) {
      if (thisArg instanceof RegExp) {
        thisArg.lastIndex = 0;
      }
      for (var _len3 = arguments.length, args = new Array(_len3 > 1 ? _len3 - 1 : 0), _key3 = 1; _key3 < _len3; _key3++) {
        args[_key3 - 1] = arguments[_key3];
      }
      return apply(func, thisArg, args);
    };
  }
  function unconstruct(Func) {
    return function() {
      for (var _len4 = arguments.length, args = new Array(_len4), _key4 = 0; _key4 < _len4; _key4++) {
        args[_key4] = arguments[_key4];
      }
      return construct(Func, args);
    };
  }
  function addToSet(set, array) {
    let transformCaseFunc = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : stringToLowerCase;
    if (setPrototypeOf) {
      setPrototypeOf(set, null);
    }
    let l = array.length;
    while (l--) {
      let element = array[l];
      if (typeof element === "string") {
        const lcElement = transformCaseFunc(element);
        if (lcElement !== element) {
          if (!isFrozen(array)) {
            array[l] = lcElement;
          }
          element = lcElement;
        }
      }
      set[element] = true;
    }
    return set;
  }
  function cleanArray(array) {
    for (let index = 0; index < array.length; index++) {
      const isPropertyExist = objectHasOwnProperty(array, index);
      if (!isPropertyExist) {
        array[index] = null;
      }
    }
    return array;
  }
  function clone(object) {
    const newObject = create(null);
    for (const [property, value] of entries(object)) {
      const isPropertyExist = objectHasOwnProperty(object, property);
      if (isPropertyExist) {
        if (Array.isArray(value)) {
          newObject[property] = cleanArray(value);
        } else if (value && typeof value === "object" && value.constructor === Object) {
          newObject[property] = clone(value);
        } else {
          newObject[property] = value;
        }
      }
    }
    return newObject;
  }
  function lookupGetter(object, prop) {
    while (object !== null) {
      const desc = getOwnPropertyDescriptor(object, prop);
      if (desc) {
        if (desc.get) {
          return unapply(desc.get);
        }
        if (typeof desc.value === "function") {
          return unapply(desc.value);
        }
      }
      object = getPrototypeOf(object);
    }
    function fallbackValue() {
      return null;
    }
    return fallbackValue;
  }
  const html$1 = freeze(["a", "abbr", "acronym", "address", "area", "article", "aside", "audio", "b", "bdi", "bdo", "big", "blink", "blockquote", "body", "br", "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "content", "data", "datalist", "dd", "decorator", "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", "element", "em", "fieldset", "figcaption", "figure", "font", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "img", "input", "ins", "kbd", "label", "legend", "li", "main", "map", "mark", "marquee", "menu", "menuitem", "meter", "nav", "nobr", "ol", "optgroup", "option", "output", "p", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "search", "section", "select", "shadow", "slot", "small", "source", "spacer", "span", "strike", "strong", "style", "sub", "summary", "sup", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "tr", "track", "tt", "u", "ul", "var", "video", "wbr"]);
  const svg$1 = freeze(["svg", "a", "altglyph", "altglyphdef", "altglyphitem", "animatecolor", "animatemotion", "animatetransform", "circle", "clippath", "defs", "desc", "ellipse", "enterkeyhint", "exportparts", "filter", "font", "g", "glyph", "glyphref", "hkern", "image", "inputmode", "line", "lineargradient", "marker", "mask", "metadata", "mpath", "part", "path", "pattern", "polygon", "polyline", "radialgradient", "rect", "stop", "style", "switch", "symbol", "text", "textpath", "title", "tref", "tspan", "view", "vkern"]);
  const svgFilters = freeze(["feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence"]);
  const svgDisallowed = freeze(["animate", "color-profile", "cursor", "discard", "font-face", "font-face-format", "font-face-name", "font-face-src", "font-face-uri", "foreignobject", "hatch", "hatchpath", "mesh", "meshgradient", "meshpatch", "meshrow", "missing-glyph", "script", "set", "solidcolor", "unknown", "use"]);
  const mathMl$1 = freeze(["math", "menclose", "merror", "mfenced", "mfrac", "mglyph", "mi", "mlabeledtr", "mmultiscripts", "mn", "mo", "mover", "mpadded", "mphantom", "mroot", "mrow", "ms", "mspace", "msqrt", "mstyle", "msub", "msup", "msubsup", "mtable", "mtd", "mtext", "mtr", "munder", "munderover", "mprescripts"]);
  const mathMlDisallowed = freeze(["maction", "maligngroup", "malignmark", "mlongdiv", "mscarries", "mscarry", "msgroup", "mstack", "msline", "msrow", "semantics", "annotation", "annotation-xml", "mprescripts", "none"]);
  const text = freeze(["#text"]);
  const html = freeze(["accept", "action", "align", "alt", "autocapitalize", "autocomplete", "autopictureinpicture", "autoplay", "background", "bgcolor", "border", "capture", "cellpadding", "cellspacing", "checked", "cite", "class", "clear", "color", "cols", "colspan", "controls", "controlslist", "coords", "crossorigin", "datetime", "decoding", "default", "dir", "disabled", "disablepictureinpicture", "disableremoteplayback", "download", "draggable", "enctype", "enterkeyhint", "exportparts", "face", "for", "headers", "height", "hidden", "high", "href", "hreflang", "id", "inert", "inputmode", "integrity", "ismap", "kind", "label", "lang", "list", "loading", "loop", "low", "max", "maxlength", "media", "method", "min", "minlength", "multiple", "muted", "name", "nonce", "noshade", "novalidate", "nowrap", "open", "optimum", "part", "pattern", "placeholder", "playsinline", "popover", "popovertarget", "popovertargetaction", "poster", "preload", "pubdate", "radiogroup", "readonly", "rel", "required", "rev", "reversed", "role", "rows", "rowspan", "spellcheck", "scope", "selected", "shape", "size", "sizes", "slot", "span", "srclang", "start", "src", "srcset", "step", "style", "summary", "tabindex", "title", "translate", "type", "usemap", "valign", "value", "width", "wrap", "xmlns", "slot"]);
  const svg = freeze(["accent-height", "accumulate", "additive", "alignment-baseline", "amplitude", "ascent", "attributename", "attributetype", "azimuth", "basefrequency", "baseline-shift", "begin", "bias", "by", "class", "clip", "clippathunits", "clip-path", "clip-rule", "color", "color-interpolation", "color-interpolation-filters", "color-profile", "color-rendering", "cx", "cy", "d", "dx", "dy", "diffuseconstant", "direction", "display", "divisor", "dur", "edgemode", "elevation", "end", "exponent", "fill", "fill-opacity", "fill-rule", "filter", "filterunits", "flood-color", "flood-opacity", "font-family", "font-size", "font-size-adjust", "font-stretch", "font-style", "font-variant", "font-weight", "fx", "fy", "g1", "g2", "glyph-name", "glyphref", "gradientunits", "gradienttransform", "height", "href", "id", "image-rendering", "in", "in2", "intercept", "k", "k1", "k2", "k3", "k4", "kerning", "keypoints", "keysplines", "keytimes", "lang", "lengthadjust", "letter-spacing", "kernelmatrix", "kernelunitlength", "lighting-color", "local", "marker-end", "marker-mid", "marker-start", "markerheight", "markerunits", "markerwidth", "maskcontentunits", "maskunits", "max", "mask", "mask-type", "media", "method", "mode", "min", "name", "numoctaves", "offset", "operator", "opacity", "order", "orient", "orientation", "origin", "overflow", "paint-order", "path", "pathlength", "patterncontentunits", "patterntransform", "patternunits", "points", "preservealpha", "preserveaspectratio", "primitiveunits", "r", "rx", "ry", "radius", "refx", "refy", "repeatcount", "repeatdur", "restart", "result", "rotate", "scale", "seed", "shape-rendering", "slope", "specularconstant", "specularexponent", "spreadmethod", "startoffset", "stddeviation", "stitchtiles", "stop-color", "stop-opacity", "stroke-dasharray", "stroke-dashoffset", "stroke-linecap", "stroke-linejoin", "stroke-miterlimit", "stroke-opacity", "stroke", "stroke-width", "style", "surfacescale", "systemlanguage", "tabindex", "tablevalues", "targetx", "targety", "transform", "transform-origin", "text-anchor", "text-decoration", "text-rendering", "textlength", "type", "u1", "u2", "unicode", "values", "viewbox", "visibility", "version", "vert-adv-y", "vert-origin-x", "vert-origin-y", "width", "word-spacing", "wrap", "writing-mode", "xchannelselector", "ychannelselector", "x", "x1", "x2", "xmlns", "y", "y1", "y2", "z", "zoomandpan"]);
  const mathMl = freeze(["accent", "accentunder", "align", "bevelled", "close", "columnalign", "columnlines", "columnspacing", "columnspan", "denomalign", "depth", "dir", "display", "displaystyle", "encoding", "fence", "frame", "height", "href", "id", "largeop", "length", "linethickness", "lquote", "lspace", "mathbackground", "mathcolor", "mathsize", "mathvariant", "maxsize", "minsize", "movablelimits", "notation", "numalign", "open", "rowalign", "rowlines", "rowspacing", "rowspan", "rspace", "rquote", "scriptlevel", "scriptminsize", "scriptsizemultiplier", "selection", "separator", "separators", "stretchy", "subscriptshift", "supscriptshift", "symmetric", "voffset", "width", "xmlns"]);
  const xml = freeze(["xlink:href", "xml:id", "xlink:title", "xml:space", "xmlns:xlink"]);
  const MUSTACHE_EXPR = seal(/\{\{[\w\W]*|[\w\W]*\}\}/gm);
  const ERB_EXPR = seal(/<%[\w\W]*|[\w\W]*%>/gm);
  const TMPLIT_EXPR = seal(/\$\{[\w\W]*/gm);
  const DATA_ATTR = seal(/^data-[\-\w.\u00B7-\uFFFF]+$/);
  const ARIA_ATTR = seal(/^aria-[\-\w]+$/);
  const IS_ALLOWED_URI = seal(
    /^(?:(?:(?:f|ht)tps?|mailto|tel|callto|sms|cid|xmpp|matrix):|[^a-z]|[a-z+.\-]+(?:[^a-z+.\-:]|$))/i
    // eslint-disable-line no-useless-escape
  );
  const IS_SCRIPT_OR_DATA = seal(/^(?:\w+script|data):/i);
  const ATTR_WHITESPACE = seal(
    /[\u0000-\u0020\u00A0\u1680\u180E\u2000-\u2029\u205F\u3000]/g
    // eslint-disable-line no-control-regex
  );
  const DOCTYPE_NAME = seal(/^html$/i);
  const CUSTOM_ELEMENT = seal(/^[a-z][.\w]*(-[.\w]+)+$/i);
  var EXPRESSIONS = /* @__PURE__ */ Object.freeze({
    __proto__: null,
    ARIA_ATTR,
    ATTR_WHITESPACE,
    CUSTOM_ELEMENT,
    DATA_ATTR,
    DOCTYPE_NAME,
    ERB_EXPR,
    IS_ALLOWED_URI,
    IS_SCRIPT_OR_DATA,
    MUSTACHE_EXPR,
    TMPLIT_EXPR
  });
  const NODE_TYPE = {
    element: 1,
    text: 3,
    // Deprecated
    progressingInstruction: 7,
    comment: 8,
    document: 9
  };
  const getGlobal = function getGlobal2() {
    return typeof window === "undefined" ? null : window;
  };
  const _createTrustedTypesPolicy = function _createTrustedTypesPolicy2(trustedTypes, purifyHostElement) {
    if (typeof trustedTypes !== "object" || typeof trustedTypes.createPolicy !== "function") {
      return null;
    }
    let suffix = null;
    const ATTR_NAME = "data-tt-policy-suffix";
    if (purifyHostElement && purifyHostElement.hasAttribute(ATTR_NAME)) {
      suffix = purifyHostElement.getAttribute(ATTR_NAME);
    }
    const policyName = "dompurify" + (suffix ? "#" + suffix : "");
    try {
      return trustedTypes.createPolicy(policyName, {
        createHTML(html2) {
          return html2;
        },
        createScriptURL(scriptUrl) {
          return scriptUrl;
        }
      });
    } catch (_) {
      console.warn("TrustedTypes policy " + policyName + " could not be created.");
      return null;
    }
  };
  const _createHooksMap = function _createHooksMap2() {
    return {
      afterSanitizeAttributes: [],
      afterSanitizeElements: [],
      afterSanitizeShadowDOM: [],
      beforeSanitizeAttributes: [],
      beforeSanitizeElements: [],
      beforeSanitizeShadowDOM: [],
      uponSanitizeAttribute: [],
      uponSanitizeElement: [],
      uponSanitizeShadowNode: []
    };
  };
  function createDOMPurify() {
    let window2 = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : getGlobal();
    const DOMPurify = (root) => createDOMPurify(root);
    DOMPurify.version = "3.4.0";
    DOMPurify.removed = [];
    if (!window2 || !window2.document || window2.document.nodeType !== NODE_TYPE.document || !window2.Element) {
      DOMPurify.isSupported = false;
      return DOMPurify;
    }
    let {
      document: document2
    } = window2;
    const originalDocument = document2;
    const currentScript = originalDocument.currentScript;
    const {
      DocumentFragment,
      HTMLTemplateElement,
      Node,
      Element,
      NodeFilter,
      NamedNodeMap = window2.NamedNodeMap || window2.MozNamedAttrMap,
      HTMLFormElement,
      DOMParser,
      trustedTypes
    } = window2;
    const ElementPrototype = Element.prototype;
    const cloneNode = lookupGetter(ElementPrototype, "cloneNode");
    const remove = lookupGetter(ElementPrototype, "remove");
    const getNextSibling = lookupGetter(ElementPrototype, "nextSibling");
    const getChildNodes = lookupGetter(ElementPrototype, "childNodes");
    const getParentNode = lookupGetter(ElementPrototype, "parentNode");
    if (typeof HTMLTemplateElement === "function") {
      const template = document2.createElement("template");
      if (template.content && template.content.ownerDocument) {
        document2 = template.content.ownerDocument;
      }
    }
    let trustedTypesPolicy;
    let emptyHTML = "";
    const {
      implementation,
      createNodeIterator,
      createDocumentFragment,
      getElementsByTagName
    } = document2;
    const {
      importNode
    } = originalDocument;
    let hooks = _createHooksMap();
    DOMPurify.isSupported = typeof entries === "function" && typeof getParentNode === "function" && implementation && implementation.createHTMLDocument !== void 0;
    const {
      MUSTACHE_EXPR: MUSTACHE_EXPR2,
      ERB_EXPR: ERB_EXPR2,
      TMPLIT_EXPR: TMPLIT_EXPR2,
      DATA_ATTR: DATA_ATTR2,
      ARIA_ATTR: ARIA_ATTR2,
      IS_SCRIPT_OR_DATA: IS_SCRIPT_OR_DATA2,
      ATTR_WHITESPACE: ATTR_WHITESPACE2,
      CUSTOM_ELEMENT: CUSTOM_ELEMENT2
    } = EXPRESSIONS;
    let {
      IS_ALLOWED_URI: IS_ALLOWED_URI$1
    } = EXPRESSIONS;
    let ALLOWED_TAGS = null;
    const DEFAULT_ALLOWED_TAGS = addToSet({}, [...html$1, ...svg$1, ...svgFilters, ...mathMl$1, ...text]);
    let ALLOWED_ATTR = null;
    const DEFAULT_ALLOWED_ATTR = addToSet({}, [...html, ...svg, ...mathMl, ...xml]);
    let CUSTOM_ELEMENT_HANDLING = Object.seal(create(null, {
      tagNameCheck: {
        writable: true,
        configurable: false,
        enumerable: true,
        value: null
      },
      attributeNameCheck: {
        writable: true,
        configurable: false,
        enumerable: true,
        value: null
      },
      allowCustomizedBuiltInElements: {
        writable: true,
        configurable: false,
        enumerable: true,
        value: false
      }
    }));
    let FORBID_TAGS = null;
    let FORBID_ATTR = null;
    const EXTRA_ELEMENT_HANDLING = Object.seal(create(null, {
      tagCheck: {
        writable: true,
        configurable: false,
        enumerable: true,
        value: null
      },
      attributeCheck: {
        writable: true,
        configurable: false,
        enumerable: true,
        value: null
      }
    }));
    let ALLOW_ARIA_ATTR = true;
    let ALLOW_DATA_ATTR = true;
    let ALLOW_UNKNOWN_PROTOCOLS = false;
    let ALLOW_SELF_CLOSE_IN_ATTR = true;
    let SAFE_FOR_TEMPLATES = false;
    let SAFE_FOR_XML = true;
    let WHOLE_DOCUMENT = false;
    let SET_CONFIG = false;
    let FORCE_BODY = false;
    let RETURN_DOM = false;
    let RETURN_DOM_FRAGMENT = false;
    let RETURN_TRUSTED_TYPE = false;
    let SANITIZE_DOM = true;
    let SANITIZE_NAMED_PROPS = false;
    const SANITIZE_NAMED_PROPS_PREFIX = "user-content-";
    let KEEP_CONTENT = true;
    let IN_PLACE = false;
    let USE_PROFILES = {};
    let FORBID_CONTENTS = null;
    const DEFAULT_FORBID_CONTENTS = addToSet({}, ["annotation-xml", "audio", "colgroup", "desc", "foreignobject", "head", "iframe", "math", "mi", "mn", "mo", "ms", "mtext", "noembed", "noframes", "noscript", "plaintext", "script", "style", "svg", "template", "thead", "title", "video", "xmp"]);
    let DATA_URI_TAGS = null;
    const DEFAULT_DATA_URI_TAGS = addToSet({}, ["audio", "video", "img", "source", "image", "track"]);
    let URI_SAFE_ATTRIBUTES = null;
    const DEFAULT_URI_SAFE_ATTRIBUTES = addToSet({}, ["alt", "class", "for", "id", "label", "name", "pattern", "placeholder", "role", "summary", "title", "value", "style", "xmlns"]);
    const MATHML_NAMESPACE = "http://www.w3.org/1998/Math/MathML";
    const SVG_NAMESPACE = "http://www.w3.org/2000/svg";
    const HTML_NAMESPACE = "http://www.w3.org/1999/xhtml";
    let NAMESPACE = HTML_NAMESPACE;
    let IS_EMPTY_INPUT = false;
    let ALLOWED_NAMESPACES = null;
    const DEFAULT_ALLOWED_NAMESPACES = addToSet({}, [MATHML_NAMESPACE, SVG_NAMESPACE, HTML_NAMESPACE], stringToString);
    let MATHML_TEXT_INTEGRATION_POINTS = addToSet({}, ["mi", "mo", "mn", "ms", "mtext"]);
    let HTML_INTEGRATION_POINTS = addToSet({}, ["annotation-xml"]);
    const COMMON_SVG_AND_HTML_ELEMENTS = addToSet({}, ["title", "style", "font", "a", "script"]);
    let PARSER_MEDIA_TYPE = null;
    const SUPPORTED_PARSER_MEDIA_TYPES = ["application/xhtml+xml", "text/html"];
    const DEFAULT_PARSER_MEDIA_TYPE = "text/html";
    let transformCaseFunc = null;
    let CONFIG = null;
    const formElement = document2.createElement("form");
    const isRegexOrFunction = function isRegexOrFunction2(testValue) {
      return testValue instanceof RegExp || testValue instanceof Function;
    };
    const _parseConfig = function _parseConfig2() {
      let cfg = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
      if (CONFIG && CONFIG === cfg) {
        return;
      }
      if (!cfg || typeof cfg !== "object") {
        cfg = {};
      }
      cfg = clone(cfg);
      PARSER_MEDIA_TYPE = // eslint-disable-next-line unicorn/prefer-includes
      SUPPORTED_PARSER_MEDIA_TYPES.indexOf(cfg.PARSER_MEDIA_TYPE) === -1 ? DEFAULT_PARSER_MEDIA_TYPE : cfg.PARSER_MEDIA_TYPE;
      transformCaseFunc = PARSER_MEDIA_TYPE === "application/xhtml+xml" ? stringToString : stringToLowerCase;
      ALLOWED_TAGS = objectHasOwnProperty(cfg, "ALLOWED_TAGS") ? addToSet({}, cfg.ALLOWED_TAGS, transformCaseFunc) : DEFAULT_ALLOWED_TAGS;
      ALLOWED_ATTR = objectHasOwnProperty(cfg, "ALLOWED_ATTR") ? addToSet({}, cfg.ALLOWED_ATTR, transformCaseFunc) : DEFAULT_ALLOWED_ATTR;
      ALLOWED_NAMESPACES = objectHasOwnProperty(cfg, "ALLOWED_NAMESPACES") ? addToSet({}, cfg.ALLOWED_NAMESPACES, stringToString) : DEFAULT_ALLOWED_NAMESPACES;
      URI_SAFE_ATTRIBUTES = objectHasOwnProperty(cfg, "ADD_URI_SAFE_ATTR") ? addToSet(clone(DEFAULT_URI_SAFE_ATTRIBUTES), cfg.ADD_URI_SAFE_ATTR, transformCaseFunc) : DEFAULT_URI_SAFE_ATTRIBUTES;
      DATA_URI_TAGS = objectHasOwnProperty(cfg, "ADD_DATA_URI_TAGS") ? addToSet(clone(DEFAULT_DATA_URI_TAGS), cfg.ADD_DATA_URI_TAGS, transformCaseFunc) : DEFAULT_DATA_URI_TAGS;
      FORBID_CONTENTS = objectHasOwnProperty(cfg, "FORBID_CONTENTS") ? addToSet({}, cfg.FORBID_CONTENTS, transformCaseFunc) : DEFAULT_FORBID_CONTENTS;
      FORBID_TAGS = objectHasOwnProperty(cfg, "FORBID_TAGS") ? addToSet({}, cfg.FORBID_TAGS, transformCaseFunc) : clone({});
      FORBID_ATTR = objectHasOwnProperty(cfg, "FORBID_ATTR") ? addToSet({}, cfg.FORBID_ATTR, transformCaseFunc) : clone({});
      USE_PROFILES = objectHasOwnProperty(cfg, "USE_PROFILES") ? cfg.USE_PROFILES : false;
      ALLOW_ARIA_ATTR = cfg.ALLOW_ARIA_ATTR !== false;
      ALLOW_DATA_ATTR = cfg.ALLOW_DATA_ATTR !== false;
      ALLOW_UNKNOWN_PROTOCOLS = cfg.ALLOW_UNKNOWN_PROTOCOLS || false;
      ALLOW_SELF_CLOSE_IN_ATTR = cfg.ALLOW_SELF_CLOSE_IN_ATTR !== false;
      SAFE_FOR_TEMPLATES = cfg.SAFE_FOR_TEMPLATES || false;
      SAFE_FOR_XML = cfg.SAFE_FOR_XML !== false;
      WHOLE_DOCUMENT = cfg.WHOLE_DOCUMENT || false;
      RETURN_DOM = cfg.RETURN_DOM || false;
      RETURN_DOM_FRAGMENT = cfg.RETURN_DOM_FRAGMENT || false;
      RETURN_TRUSTED_TYPE = cfg.RETURN_TRUSTED_TYPE || false;
      FORCE_BODY = cfg.FORCE_BODY || false;
      SANITIZE_DOM = cfg.SANITIZE_DOM !== false;
      SANITIZE_NAMED_PROPS = cfg.SANITIZE_NAMED_PROPS || false;
      KEEP_CONTENT = cfg.KEEP_CONTENT !== false;
      IN_PLACE = cfg.IN_PLACE || false;
      IS_ALLOWED_URI$1 = cfg.ALLOWED_URI_REGEXP || IS_ALLOWED_URI;
      NAMESPACE = cfg.NAMESPACE || HTML_NAMESPACE;
      MATHML_TEXT_INTEGRATION_POINTS = cfg.MATHML_TEXT_INTEGRATION_POINTS || MATHML_TEXT_INTEGRATION_POINTS;
      HTML_INTEGRATION_POINTS = cfg.HTML_INTEGRATION_POINTS || HTML_INTEGRATION_POINTS;
      CUSTOM_ELEMENT_HANDLING = cfg.CUSTOM_ELEMENT_HANDLING || create(null);
      if (cfg.CUSTOM_ELEMENT_HANDLING && isRegexOrFunction(cfg.CUSTOM_ELEMENT_HANDLING.tagNameCheck)) {
        CUSTOM_ELEMENT_HANDLING.tagNameCheck = cfg.CUSTOM_ELEMENT_HANDLING.tagNameCheck;
      }
      if (cfg.CUSTOM_ELEMENT_HANDLING && isRegexOrFunction(cfg.CUSTOM_ELEMENT_HANDLING.attributeNameCheck)) {
        CUSTOM_ELEMENT_HANDLING.attributeNameCheck = cfg.CUSTOM_ELEMENT_HANDLING.attributeNameCheck;
      }
      if (cfg.CUSTOM_ELEMENT_HANDLING && typeof cfg.CUSTOM_ELEMENT_HANDLING.allowCustomizedBuiltInElements === "boolean") {
        CUSTOM_ELEMENT_HANDLING.allowCustomizedBuiltInElements = cfg.CUSTOM_ELEMENT_HANDLING.allowCustomizedBuiltInElements;
      }
      if (SAFE_FOR_TEMPLATES) {
        ALLOW_DATA_ATTR = false;
      }
      if (RETURN_DOM_FRAGMENT) {
        RETURN_DOM = true;
      }
      if (USE_PROFILES) {
        ALLOWED_TAGS = addToSet({}, text);
        ALLOWED_ATTR = create(null);
        if (USE_PROFILES.html === true) {
          addToSet(ALLOWED_TAGS, html$1);
          addToSet(ALLOWED_ATTR, html);
        }
        if (USE_PROFILES.svg === true) {
          addToSet(ALLOWED_TAGS, svg$1);
          addToSet(ALLOWED_ATTR, svg);
          addToSet(ALLOWED_ATTR, xml);
        }
        if (USE_PROFILES.svgFilters === true) {
          addToSet(ALLOWED_TAGS, svgFilters);
          addToSet(ALLOWED_ATTR, svg);
          addToSet(ALLOWED_ATTR, xml);
        }
        if (USE_PROFILES.mathMl === true) {
          addToSet(ALLOWED_TAGS, mathMl$1);
          addToSet(ALLOWED_ATTR, mathMl);
          addToSet(ALLOWED_ATTR, xml);
        }
      }
      EXTRA_ELEMENT_HANDLING.tagCheck = null;
      EXTRA_ELEMENT_HANDLING.attributeCheck = null;
      if (cfg.ADD_TAGS) {
        if (typeof cfg.ADD_TAGS === "function") {
          EXTRA_ELEMENT_HANDLING.tagCheck = cfg.ADD_TAGS;
        } else {
          if (ALLOWED_TAGS === DEFAULT_ALLOWED_TAGS) {
            ALLOWED_TAGS = clone(ALLOWED_TAGS);
          }
          addToSet(ALLOWED_TAGS, cfg.ADD_TAGS, transformCaseFunc);
        }
      }
      if (cfg.ADD_ATTR) {
        if (typeof cfg.ADD_ATTR === "function") {
          EXTRA_ELEMENT_HANDLING.attributeCheck = cfg.ADD_ATTR;
        } else {
          if (ALLOWED_ATTR === DEFAULT_ALLOWED_ATTR) {
            ALLOWED_ATTR = clone(ALLOWED_ATTR);
          }
          addToSet(ALLOWED_ATTR, cfg.ADD_ATTR, transformCaseFunc);
        }
      }
      if (cfg.ADD_URI_SAFE_ATTR) {
        addToSet(URI_SAFE_ATTRIBUTES, cfg.ADD_URI_SAFE_ATTR, transformCaseFunc);
      }
      if (cfg.FORBID_CONTENTS) {
        if (FORBID_CONTENTS === DEFAULT_FORBID_CONTENTS) {
          FORBID_CONTENTS = clone(FORBID_CONTENTS);
        }
        addToSet(FORBID_CONTENTS, cfg.FORBID_CONTENTS, transformCaseFunc);
      }
      if (cfg.ADD_FORBID_CONTENTS) {
        if (FORBID_CONTENTS === DEFAULT_FORBID_CONTENTS) {
          FORBID_CONTENTS = clone(FORBID_CONTENTS);
        }
        addToSet(FORBID_CONTENTS, cfg.ADD_FORBID_CONTENTS, transformCaseFunc);
      }
      if (KEEP_CONTENT) {
        ALLOWED_TAGS["#text"] = true;
      }
      if (WHOLE_DOCUMENT) {
        addToSet(ALLOWED_TAGS, ["html", "head", "body"]);
      }
      if (ALLOWED_TAGS.table) {
        addToSet(ALLOWED_TAGS, ["tbody"]);
        delete FORBID_TAGS.tbody;
      }
      if (cfg.TRUSTED_TYPES_POLICY) {
        if (typeof cfg.TRUSTED_TYPES_POLICY.createHTML !== "function") {
          throw typeErrorCreate('TRUSTED_TYPES_POLICY configuration option must provide a "createHTML" hook.');
        }
        if (typeof cfg.TRUSTED_TYPES_POLICY.createScriptURL !== "function") {
          throw typeErrorCreate('TRUSTED_TYPES_POLICY configuration option must provide a "createScriptURL" hook.');
        }
        trustedTypesPolicy = cfg.TRUSTED_TYPES_POLICY;
        emptyHTML = trustedTypesPolicy.createHTML("");
      } else {
        if (trustedTypesPolicy === void 0) {
          trustedTypesPolicy = _createTrustedTypesPolicy(trustedTypes, currentScript);
        }
        if (trustedTypesPolicy !== null && typeof emptyHTML === "string") {
          emptyHTML = trustedTypesPolicy.createHTML("");
        }
      }
      if (freeze) {
        freeze(cfg);
      }
      CONFIG = cfg;
    };
    const ALL_SVG_TAGS = addToSet({}, [...svg$1, ...svgFilters, ...svgDisallowed]);
    const ALL_MATHML_TAGS = addToSet({}, [...mathMl$1, ...mathMlDisallowed]);
    const _checkValidNamespace = function _checkValidNamespace2(element) {
      let parent = getParentNode(element);
      if (!parent || !parent.tagName) {
        parent = {
          namespaceURI: NAMESPACE,
          tagName: "template"
        };
      }
      const tagName = stringToLowerCase(element.tagName);
      const parentTagName = stringToLowerCase(parent.tagName);
      if (!ALLOWED_NAMESPACES[element.namespaceURI]) {
        return false;
      }
      if (element.namespaceURI === SVG_NAMESPACE) {
        if (parent.namespaceURI === HTML_NAMESPACE) {
          return tagName === "svg";
        }
        if (parent.namespaceURI === MATHML_NAMESPACE) {
          return tagName === "svg" && (parentTagName === "annotation-xml" || MATHML_TEXT_INTEGRATION_POINTS[parentTagName]);
        }
        return Boolean(ALL_SVG_TAGS[tagName]);
      }
      if (element.namespaceURI === MATHML_NAMESPACE) {
        if (parent.namespaceURI === HTML_NAMESPACE) {
          return tagName === "math";
        }
        if (parent.namespaceURI === SVG_NAMESPACE) {
          return tagName === "math" && HTML_INTEGRATION_POINTS[parentTagName];
        }
        return Boolean(ALL_MATHML_TAGS[tagName]);
      }
      if (element.namespaceURI === HTML_NAMESPACE) {
        if (parent.namespaceURI === SVG_NAMESPACE && !HTML_INTEGRATION_POINTS[parentTagName]) {
          return false;
        }
        if (parent.namespaceURI === MATHML_NAMESPACE && !MATHML_TEXT_INTEGRATION_POINTS[parentTagName]) {
          return false;
        }
        return !ALL_MATHML_TAGS[tagName] && (COMMON_SVG_AND_HTML_ELEMENTS[tagName] || !ALL_SVG_TAGS[tagName]);
      }
      if (PARSER_MEDIA_TYPE === "application/xhtml+xml" && ALLOWED_NAMESPACES[element.namespaceURI]) {
        return true;
      }
      return false;
    };
    const _forceRemove = function _forceRemove2(node) {
      arrayPush(DOMPurify.removed, {
        element: node
      });
      try {
        getParentNode(node).removeChild(node);
      } catch (_) {
        remove(node);
      }
    };
    const _removeAttribute = function _removeAttribute2(name, element) {
      try {
        arrayPush(DOMPurify.removed, {
          attribute: element.getAttributeNode(name),
          from: element
        });
      } catch (_) {
        arrayPush(DOMPurify.removed, {
          attribute: null,
          from: element
        });
      }
      element.removeAttribute(name);
      if (name === "is") {
        if (RETURN_DOM || RETURN_DOM_FRAGMENT) {
          try {
            _forceRemove(element);
          } catch (_) {
          }
        } else {
          try {
            element.setAttribute(name, "");
          } catch (_) {
          }
        }
      }
    };
    const _initDocument = function _initDocument2(dirty) {
      let doc = null;
      let leadingWhitespace = null;
      if (FORCE_BODY) {
        dirty = "<remove></remove>" + dirty;
      } else {
        const matches = stringMatch(dirty, /^[\r\n\t ]+/);
        leadingWhitespace = matches && matches[0];
      }
      if (PARSER_MEDIA_TYPE === "application/xhtml+xml" && NAMESPACE === HTML_NAMESPACE) {
        dirty = '<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>' + dirty + "</body></html>";
      }
      const dirtyPayload = trustedTypesPolicy ? trustedTypesPolicy.createHTML(dirty) : dirty;
      if (NAMESPACE === HTML_NAMESPACE) {
        try {
          doc = new DOMParser().parseFromString(dirtyPayload, PARSER_MEDIA_TYPE);
        } catch (_) {
        }
      }
      if (!doc || !doc.documentElement) {
        doc = implementation.createDocument(NAMESPACE, "template", null);
        try {
          doc.documentElement.innerHTML = IS_EMPTY_INPUT ? emptyHTML : dirtyPayload;
        } catch (_) {
        }
      }
      const body = doc.body || doc.documentElement;
      if (dirty && leadingWhitespace) {
        body.insertBefore(document2.createTextNode(leadingWhitespace), body.childNodes[0] || null);
      }
      if (NAMESPACE === HTML_NAMESPACE) {
        return getElementsByTagName.call(doc, WHOLE_DOCUMENT ? "html" : "body")[0];
      }
      return WHOLE_DOCUMENT ? doc.documentElement : body;
    };
    const _createNodeIterator = function _createNodeIterator2(root) {
      return createNodeIterator.call(
        root.ownerDocument || root,
        root,
        // eslint-disable-next-line no-bitwise
        NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_COMMENT | NodeFilter.SHOW_TEXT | NodeFilter.SHOW_PROCESSING_INSTRUCTION | NodeFilter.SHOW_CDATA_SECTION,
        null
      );
    };
    const _isClobbered = function _isClobbered2(element) {
      return element instanceof HTMLFormElement && (typeof element.nodeName !== "string" || typeof element.textContent !== "string" || typeof element.removeChild !== "function" || !(element.attributes instanceof NamedNodeMap) || typeof element.removeAttribute !== "function" || typeof element.setAttribute !== "function" || typeof element.namespaceURI !== "string" || typeof element.insertBefore !== "function" || typeof element.hasChildNodes !== "function");
    };
    const _isNode = function _isNode2(value) {
      return typeof Node === "function" && value instanceof Node;
    };
    function _executeHooks(hooks2, currentNode, data) {
      arrayForEach(hooks2, (hook) => {
        hook.call(DOMPurify, currentNode, data, CONFIG);
      });
    }
    const _sanitizeElements = function _sanitizeElements2(currentNode) {
      let content = null;
      _executeHooks(hooks.beforeSanitizeElements, currentNode, null);
      if (_isClobbered(currentNode)) {
        _forceRemove(currentNode);
        return true;
      }
      const tagName = transformCaseFunc(currentNode.nodeName);
      _executeHooks(hooks.uponSanitizeElement, currentNode, {
        tagName,
        allowedTags: ALLOWED_TAGS
      });
      if (SAFE_FOR_XML && currentNode.hasChildNodes() && !_isNode(currentNode.firstElementChild) && regExpTest(/<[/\w!]/g, currentNode.innerHTML) && regExpTest(/<[/\w!]/g, currentNode.textContent)) {
        _forceRemove(currentNode);
        return true;
      }
      if (SAFE_FOR_XML && currentNode.namespaceURI === HTML_NAMESPACE && tagName === "style" && _isNode(currentNode.firstElementChild)) {
        _forceRemove(currentNode);
        return true;
      }
      if (currentNode.nodeType === NODE_TYPE.progressingInstruction) {
        _forceRemove(currentNode);
        return true;
      }
      if (SAFE_FOR_XML && currentNode.nodeType === NODE_TYPE.comment && regExpTest(/<[/\w]/g, currentNode.data)) {
        _forceRemove(currentNode);
        return true;
      }
      if (FORBID_TAGS[tagName] || !(EXTRA_ELEMENT_HANDLING.tagCheck instanceof Function && EXTRA_ELEMENT_HANDLING.tagCheck(tagName)) && !ALLOWED_TAGS[tagName]) {
        if (!FORBID_TAGS[tagName] && _isBasicCustomElement(tagName)) {
          if (CUSTOM_ELEMENT_HANDLING.tagNameCheck instanceof RegExp && regExpTest(CUSTOM_ELEMENT_HANDLING.tagNameCheck, tagName)) {
            return false;
          }
          if (CUSTOM_ELEMENT_HANDLING.tagNameCheck instanceof Function && CUSTOM_ELEMENT_HANDLING.tagNameCheck(tagName)) {
            return false;
          }
        }
        if (KEEP_CONTENT && !FORBID_CONTENTS[tagName]) {
          const parentNode = getParentNode(currentNode) || currentNode.parentNode;
          const childNodes = getChildNodes(currentNode) || currentNode.childNodes;
          if (childNodes && parentNode) {
            const childCount = childNodes.length;
            for (let i = childCount - 1; i >= 0; --i) {
              const childClone = cloneNode(childNodes[i], true);
              childClone.__removalCount = (currentNode.__removalCount || 0) + 1;
              parentNode.insertBefore(childClone, getNextSibling(currentNode));
            }
          }
        }
        _forceRemove(currentNode);
        return true;
      }
      if (currentNode instanceof Element && !_checkValidNamespace(currentNode)) {
        _forceRemove(currentNode);
        return true;
      }
      if ((tagName === "noscript" || tagName === "noembed" || tagName === "noframes") && regExpTest(/<\/no(script|embed|frames)/i, currentNode.innerHTML)) {
        _forceRemove(currentNode);
        return true;
      }
      if (SAFE_FOR_TEMPLATES && currentNode.nodeType === NODE_TYPE.text) {
        content = currentNode.textContent;
        arrayForEach([MUSTACHE_EXPR2, ERB_EXPR2, TMPLIT_EXPR2], (expr) => {
          content = stringReplace(content, expr, " ");
        });
        if (currentNode.textContent !== content) {
          arrayPush(DOMPurify.removed, {
            element: currentNode.cloneNode()
          });
          currentNode.textContent = content;
        }
      }
      _executeHooks(hooks.afterSanitizeElements, currentNode, null);
      return false;
    };
    const _isValidAttribute = function _isValidAttribute2(lcTag, lcName, value) {
      if (FORBID_ATTR[lcName]) {
        return false;
      }
      if (SANITIZE_DOM && (lcName === "id" || lcName === "name") && (value in document2 || value in formElement)) {
        return false;
      }
      if (ALLOW_DATA_ATTR && !FORBID_ATTR[lcName] && regExpTest(DATA_ATTR2, lcName)) ;
      else if (ALLOW_ARIA_ATTR && regExpTest(ARIA_ATTR2, lcName)) ;
      else if (EXTRA_ELEMENT_HANDLING.attributeCheck instanceof Function && EXTRA_ELEMENT_HANDLING.attributeCheck(lcName, lcTag)) ;
      else if (!ALLOWED_ATTR[lcName] || FORBID_ATTR[lcName]) {
        if (
          // First condition does a very basic check if a) it's basically a valid custom element tagname AND
          // b) if the tagName passes whatever the user has configured for CUSTOM_ELEMENT_HANDLING.tagNameCheck
          // and c) if the attribute name passes whatever the user has configured for CUSTOM_ELEMENT_HANDLING.attributeNameCheck
          _isBasicCustomElement(lcTag) && (CUSTOM_ELEMENT_HANDLING.tagNameCheck instanceof RegExp && regExpTest(CUSTOM_ELEMENT_HANDLING.tagNameCheck, lcTag) || CUSTOM_ELEMENT_HANDLING.tagNameCheck instanceof Function && CUSTOM_ELEMENT_HANDLING.tagNameCheck(lcTag)) && (CUSTOM_ELEMENT_HANDLING.attributeNameCheck instanceof RegExp && regExpTest(CUSTOM_ELEMENT_HANDLING.attributeNameCheck, lcName) || CUSTOM_ELEMENT_HANDLING.attributeNameCheck instanceof Function && CUSTOM_ELEMENT_HANDLING.attributeNameCheck(lcName, lcTag)) || // Alternative, second condition checks if it's an `is`-attribute, AND
          // the value passes whatever the user has configured for CUSTOM_ELEMENT_HANDLING.tagNameCheck
          lcName === "is" && CUSTOM_ELEMENT_HANDLING.allowCustomizedBuiltInElements && (CUSTOM_ELEMENT_HANDLING.tagNameCheck instanceof RegExp && regExpTest(CUSTOM_ELEMENT_HANDLING.tagNameCheck, value) || CUSTOM_ELEMENT_HANDLING.tagNameCheck instanceof Function && CUSTOM_ELEMENT_HANDLING.tagNameCheck(value))
        ) ;
        else {
          return false;
        }
      } else if (URI_SAFE_ATTRIBUTES[lcName]) ;
      else if (regExpTest(IS_ALLOWED_URI$1, stringReplace(value, ATTR_WHITESPACE2, ""))) ;
      else if ((lcName === "src" || lcName === "xlink:href" || lcName === "href") && lcTag !== "script" && stringIndexOf(value, "data:") === 0 && DATA_URI_TAGS[lcTag]) ;
      else if (ALLOW_UNKNOWN_PROTOCOLS && !regExpTest(IS_SCRIPT_OR_DATA2, stringReplace(value, ATTR_WHITESPACE2, ""))) ;
      else if (value) {
        return false;
      } else ;
      return true;
    };
    const _isBasicCustomElement = function _isBasicCustomElement2(tagName) {
      return tagName !== "annotation-xml" && stringMatch(tagName, CUSTOM_ELEMENT2);
    };
    const _sanitizeAttributes = function _sanitizeAttributes2(currentNode) {
      _executeHooks(hooks.beforeSanitizeAttributes, currentNode, null);
      const {
        attributes
      } = currentNode;
      if (!attributes || _isClobbered(currentNode)) {
        return;
      }
      const hookEvent = {
        attrName: "",
        attrValue: "",
        keepAttr: true,
        allowedAttributes: ALLOWED_ATTR,
        forceKeepAttr: void 0
      };
      let l = attributes.length;
      while (l--) {
        const attr = attributes[l];
        const {
          name,
          namespaceURI,
          value: attrValue
        } = attr;
        const lcName = transformCaseFunc(name);
        const initValue = attrValue;
        let value = name === "value" ? initValue : stringTrim(initValue);
        hookEvent.attrName = lcName;
        hookEvent.attrValue = value;
        hookEvent.keepAttr = true;
        hookEvent.forceKeepAttr = void 0;
        _executeHooks(hooks.uponSanitizeAttribute, currentNode, hookEvent);
        value = hookEvent.attrValue;
        if (SANITIZE_NAMED_PROPS && (lcName === "id" || lcName === "name")) {
          _removeAttribute(name, currentNode);
          value = SANITIZE_NAMED_PROPS_PREFIX + value;
        }
        if (SAFE_FOR_XML && regExpTest(/((--!?|])>)|<\/(style|script|title|xmp|textarea|noscript|iframe|noembed|noframes)/i, value)) {
          _removeAttribute(name, currentNode);
          continue;
        }
        if (lcName === "attributename" && stringMatch(value, "href")) {
          _removeAttribute(name, currentNode);
          continue;
        }
        if (hookEvent.forceKeepAttr) {
          continue;
        }
        if (!hookEvent.keepAttr) {
          _removeAttribute(name, currentNode);
          continue;
        }
        if (!ALLOW_SELF_CLOSE_IN_ATTR && regExpTest(/\/>/i, value)) {
          _removeAttribute(name, currentNode);
          continue;
        }
        if (SAFE_FOR_TEMPLATES) {
          arrayForEach([MUSTACHE_EXPR2, ERB_EXPR2, TMPLIT_EXPR2], (expr) => {
            value = stringReplace(value, expr, " ");
          });
        }
        const lcTag = transformCaseFunc(currentNode.nodeName);
        if (!_isValidAttribute(lcTag, lcName, value)) {
          _removeAttribute(name, currentNode);
          continue;
        }
        if (trustedTypesPolicy && typeof trustedTypes === "object" && typeof trustedTypes.getAttributeType === "function") {
          if (namespaceURI) ;
          else {
            switch (trustedTypes.getAttributeType(lcTag, lcName)) {
              case "TrustedHTML": {
                value = trustedTypesPolicy.createHTML(value);
                break;
              }
              case "TrustedScriptURL": {
                value = trustedTypesPolicy.createScriptURL(value);
                break;
              }
            }
          }
        }
        if (value !== initValue) {
          try {
            if (namespaceURI) {
              currentNode.setAttributeNS(namespaceURI, name, value);
            } else {
              currentNode.setAttribute(name, value);
            }
            if (_isClobbered(currentNode)) {
              _forceRemove(currentNode);
            } else {
              arrayPop(DOMPurify.removed);
            }
          } catch (_) {
            _removeAttribute(name, currentNode);
          }
        }
      }
      _executeHooks(hooks.afterSanitizeAttributes, currentNode, null);
    };
    const _sanitizeShadowDOM2 = function _sanitizeShadowDOM(fragment) {
      let shadowNode = null;
      const shadowIterator = _createNodeIterator(fragment);
      _executeHooks(hooks.beforeSanitizeShadowDOM, fragment, null);
      while (shadowNode = shadowIterator.nextNode()) {
        _executeHooks(hooks.uponSanitizeShadowNode, shadowNode, null);
        _sanitizeElements(shadowNode);
        _sanitizeAttributes(shadowNode);
        if (shadowNode.content instanceof DocumentFragment) {
          _sanitizeShadowDOM2(shadowNode.content);
        }
      }
      _executeHooks(hooks.afterSanitizeShadowDOM, fragment, null);
    };
    DOMPurify.sanitize = function(dirty) {
      let cfg = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {};
      let body = null;
      let importedNode = null;
      let currentNode = null;
      let returnNode = null;
      IS_EMPTY_INPUT = !dirty;
      if (IS_EMPTY_INPUT) {
        dirty = "<!-->";
      }
      if (typeof dirty !== "string" && !_isNode(dirty)) {
        if (typeof dirty.toString === "function") {
          dirty = dirty.toString();
          if (typeof dirty !== "string") {
            throw typeErrorCreate("dirty is not a string, aborting");
          }
        } else {
          throw typeErrorCreate("toString is not a function");
        }
      }
      if (!DOMPurify.isSupported) {
        return dirty;
      }
      if (!SET_CONFIG) {
        _parseConfig(cfg);
      }
      DOMPurify.removed = [];
      if (typeof dirty === "string") {
        IN_PLACE = false;
      }
      if (IN_PLACE) {
        if (dirty.nodeName) {
          const tagName = transformCaseFunc(dirty.nodeName);
          if (!ALLOWED_TAGS[tagName] || FORBID_TAGS[tagName]) {
            throw typeErrorCreate("root node is forbidden and cannot be sanitized in-place");
          }
        }
      } else if (dirty instanceof Node) {
        body = _initDocument("<!---->");
        importedNode = body.ownerDocument.importNode(dirty, true);
        if (importedNode.nodeType === NODE_TYPE.element && importedNode.nodeName === "BODY") {
          body = importedNode;
        } else if (importedNode.nodeName === "HTML") {
          body = importedNode;
        } else {
          body.appendChild(importedNode);
        }
      } else {
        if (!RETURN_DOM && !SAFE_FOR_TEMPLATES && !WHOLE_DOCUMENT && // eslint-disable-next-line unicorn/prefer-includes
        dirty.indexOf("<") === -1) {
          return trustedTypesPolicy && RETURN_TRUSTED_TYPE ? trustedTypesPolicy.createHTML(dirty) : dirty;
        }
        body = _initDocument(dirty);
        if (!body) {
          return RETURN_DOM ? null : RETURN_TRUSTED_TYPE ? emptyHTML : "";
        }
      }
      if (body && FORCE_BODY) {
        _forceRemove(body.firstChild);
      }
      const nodeIterator = _createNodeIterator(IN_PLACE ? dirty : body);
      while (currentNode = nodeIterator.nextNode()) {
        _sanitizeElements(currentNode);
        _sanitizeAttributes(currentNode);
        if (currentNode.content instanceof DocumentFragment) {
          _sanitizeShadowDOM2(currentNode.content);
        }
      }
      if (IN_PLACE) {
        return dirty;
      }
      if (RETURN_DOM) {
        if (SAFE_FOR_TEMPLATES) {
          body.normalize();
          let html2 = body.innerHTML;
          arrayForEach([MUSTACHE_EXPR2, ERB_EXPR2, TMPLIT_EXPR2], (expr) => {
            html2 = stringReplace(html2, expr, " ");
          });
          body.innerHTML = html2;
        }
        if (RETURN_DOM_FRAGMENT) {
          returnNode = createDocumentFragment.call(body.ownerDocument);
          while (body.firstChild) {
            returnNode.appendChild(body.firstChild);
          }
        } else {
          returnNode = body;
        }
        if (ALLOWED_ATTR.shadowroot || ALLOWED_ATTR.shadowrootmode) {
          returnNode = importNode.call(originalDocument, returnNode, true);
        }
        return returnNode;
      }
      let serializedHTML = WHOLE_DOCUMENT ? body.outerHTML : body.innerHTML;
      if (WHOLE_DOCUMENT && ALLOWED_TAGS["!doctype"] && body.ownerDocument && body.ownerDocument.doctype && body.ownerDocument.doctype.name && regExpTest(DOCTYPE_NAME, body.ownerDocument.doctype.name)) {
        serializedHTML = "<!DOCTYPE " + body.ownerDocument.doctype.name + ">\n" + serializedHTML;
      }
      if (SAFE_FOR_TEMPLATES) {
        arrayForEach([MUSTACHE_EXPR2, ERB_EXPR2, TMPLIT_EXPR2], (expr) => {
          serializedHTML = stringReplace(serializedHTML, expr, " ");
        });
      }
      return trustedTypesPolicy && RETURN_TRUSTED_TYPE ? trustedTypesPolicy.createHTML(serializedHTML) : serializedHTML;
    };
    DOMPurify.setConfig = function() {
      let cfg = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
      _parseConfig(cfg);
      SET_CONFIG = true;
    };
    DOMPurify.clearConfig = function() {
      CONFIG = null;
      SET_CONFIG = false;
    };
    DOMPurify.isValidAttribute = function(tag, attr, value) {
      if (!CONFIG) {
        _parseConfig({});
      }
      const lcTag = transformCaseFunc(tag);
      const lcName = transformCaseFunc(attr);
      return _isValidAttribute(lcTag, lcName, value);
    };
    DOMPurify.addHook = function(entryPoint, hookFunction) {
      if (typeof hookFunction !== "function") {
        return;
      }
      arrayPush(hooks[entryPoint], hookFunction);
    };
    DOMPurify.removeHook = function(entryPoint, hookFunction) {
      if (hookFunction !== void 0) {
        const index = arrayLastIndexOf(hooks[entryPoint], hookFunction);
        return index === -1 ? void 0 : arraySplice(hooks[entryPoint], index, 1)[0];
      }
      return arrayPop(hooks[entryPoint]);
    };
    DOMPurify.removeHooks = function(entryPoint) {
      hooks[entryPoint] = [];
    };
    DOMPurify.removeAllHooks = function() {
      hooks = _createHooksMap();
    };
    return DOMPurify;
  }
  var purify = createDOMPurify();
  const emotionData = {
    "/:^_^": {
      t: "Smile",
      id: "0"
    },
    "/:^$^": {
      t: "Shy",
      id: "1"
    },
    "/:Q": {
      t: "Tongue",
      id: "2"
    },
    "/:815": {
      t: "Snicker",
      id: "3"
    },
    "/:809": {
      t: "Admire",
      id: "4"
    },
    "/:^O^": {
      t: "Laugh",
      id: "5"
    },
    "/:081": {
      t: "Dance",
      id: "6"
    },
    "/:087": {
      t: "Blow Kisses",
      id: "7"
    },
    "/:086": {
      t: "Comfort",
      id: "8"
    },
    "/:H": {
      t: "Hug",
      id: "9"
    },
    "/:012": {
      t: "Come on",
      id: "10"
    },
    "/:806": {
      t: "Victory",
      id: "11"
    },
    "/:b": {
      t: "Excellent",
      id: "12"
    },
    "/:^x^": {
      t: "Kiss",
      id: "13"
    },
    "/:814": {
      t: "Infatuated",
      id: "14"
    },
    "/:^W^": {
      t: "Grin",
      id: "15"
    },
    "/:080": {
      t: "Search",
      id: "16"
    },
    "/:066": {
      t: "Call",
      id: "17"
    },
    "/:807": {
      t: "Account",
      id: "18"
    },
    "/:805": {
      t: "Moneygrubber",
      id: "19"
    },
    "/:071": {
      t: "Good Idea",
      id: "20"
    },
    "/:072": {
      t: "Grimace",
      id: "21"
    },
    "/:065": {
      t: "Angel",
      id: "22"
    },
    "/:804": {
      t: "Bye",
      id: "23"
    },
    "/:813": {
      t: "Slobber",
      id: "24"
    },
    "/:818": {
      t: "Enjoy",
      id: "25"
    },
    "/:015": {
      t: "Erotomania",
      id: "26"
    },
    "/:084": {
      t: "Bemused",
      id: "27"
    },
    "/:801": {
      t: "Think",
      id: "28"
    },
    "/:811": {
      t: "Confused",
      id: "29"
    },
    "/:?": {
      t: "Question",
      id: "30"
    },
    "/:077": {
      t: "No Money",
      id: "31"
    },
    "/:083": {
      t: "Bored",
      id: "32"
    },
    "/:817": {
      t: "Doubt",
      id: "33"
    },
    "/:!": {
      t: "Sh",
      id: "34"
    },
    "/:068": {
      t: "Childish",
      id: "35"
    },
    "/:079": {
      t: "Shake",
      id: "36"
    },
    "/:028": {
      t: "Got a Cold",
      id: "37"
    },
    "/:026": {
      t: "Embarrassed",
      id: "38"
    },
    "/:007": {
      t: "Giggle",
      id: "39"
    },
    "/:816": {
      t: "Not Really",
      id: "40"
    },
    '/:\'""': {
      t: "No Choice",
      id: "41"
    },
    "/:802": {
      t: "Perspire",
      id: "42"
    },
    "/:027": {
      t: "Miserable",
      id: "43"
    },
    "/:(Zz...)": {
      t: "Sleepy",
      id: "44"
    },
    "/:*&*": {
      t: "Dizzy",
      id: "45"
    },
    "/:810": {
      t: "Sad",
      id: "46"
    },
    "/:>_<": {
      t: "Grievance",
      id: "47"
    },
    "/:018": {
      t: "Weep",
      id: "48"
    },
    "/:>O<": {
      t: "Cry",
      id: "49"
    },
    "/:020": {
      t: "Howl",
      id: "50"
    },
    "/:044": {
      t: "Speechless",
      id: "51"
    },
    "/:819": {
      t: "Sorry",
      id: "52"
    },
    "/:085": {
      t: "Bye",
      id: "53"
    },
    "/:812": {
      t: "Frown",
      id: "54"
    },
    '/:"': {
      t: "Tired",
      id: "55"
    },
    "/:>M<": {
      t: "Ill",
      id: "56"
    },
    "/:>@<": {
      t: "Puke",
      id: "57"
    },
    "/:076": {
      t: "Bad Luck",
      id: "58"
    },
    "/:069": {
      t: "Surprise",
      id: "59"
    },
    "/:O": {
      t: "Shock",
      id: "60"
    },
    "/:067": {
      t: "Shut up",
      id: "61"
    },
    "/:043": {
      t: "Slap",
      id: "62"
    },
    "/:P": {
      t: "Disdain",
      id: "63"
    },
    "/:808": {
      t: "Fury",
      id: "64"
    },
    "/:>W<": {
      t: "Angry",
      id: "65"
    },
    "/:073": {
      t: "God of Wealth",
      id: "66"
    },
    "/:008": {
      t: "Be Helpful",
      id: "67"
    },
    "/:803": {
      t: "Good Luck",
      id: "68"
    },
    "/:074": {
      t: "Waiter",
      id: "69"
    },
    "/:O=O": {
      t: "Boss",
      id: "70"
    },
    "/:036": {
      t: "Evil",
      id: "71"
    },
    "/:039": {
      t: "Fight Alone",
      id: "72"
    },
    "/:045": {
      t: "CS",
      id: "73"
    },
    "/:046": {
      t: "Invisible Man",
      id: "74"
    },
    "/:048": {
      t: "Bomb",
      id: "75"
    },
    "/:047": {
      t: "Scream",
      id: "76"
    },
    "/:girl": {
      t: "Beauty",
      id: "77"
    },
    "/:man": {
      t: "Handsome Guy",
      id: "78"
    },
    "/:052": {
      t: "Fortune Cat",
      id: "79"
    },
    "/:(OK)": {
      t: "OK",
      id: "80"
    },
    "/:8*8": {
      t: "Applause",
      id: "81"
    },
    "/:)-(": {
      t: "Shake Hands",
      id: "82"
    },
    "/:lip": {
      t: "Lip",
      id: "83"
    },
    "/:-F": {
      t: "Rose",
      id: "84"
    },
    "/:-W": {
      t: "Languished Rose",
      id: "85"
    },
    "/:Y": {
      t: "Love",
      id: "86"
    },
    "/:qp": {
      t: "Heartbreak",
      id: "87"
    },
    "/:$": {
      t: "Money",
      id: "88"
    },
    "/:%": {
      t: "Shopping",
      id: "89"
    },
    "/:(&)": {
      t: "Gift",
      id: "90"
    },
    "/:@": {
      t: "Mail",
      id: "91"
    },
    "/:~B": {
      t: "Phone",
      id: "92"
    },
    "/:U*U": {
      t: "Cheers",
      id: "93"
    },
    "/:clock": {
      t: "Clock",
      id: "94"
    },
    "/:R": {
      t: "Wait",
      id: "95"
    },
    "/:C": {
      t: "Late",
      id: "96"
    },
    "/:plane": {
      t: "Plane",
      id: "97"
    },
    "/:075": {
      t: "Alipay",
      id: "98"
    },
    "/:smile.": {
      t: "smile",
      id: "99"
    },
    "/:shy.": {
      t: "shy",
      id: "100"
    },
    "/:tongue.": {
      t: "tongue",
      id: "101"
    },
    "/:covermouth.": {
      t: "covermouth",
      id: "102"
    },
    "/:love.": {
      t: "love",
      id: "103"
    },
    "/:laugh.": {
      t: "laugh",
      id: "104"
    },
    "/:happy.": {
      t: "happy",
      id: "105"
    },
    "/:Blowkiss.": {
      t: "Blowkiss",
      id: "106"
    },
    "/:pathead.": {
      t: "pathead",
      id: "107"
    },
    "/:hug.": {
      t: "hug",
      id: "108"
    },
    "/:fighting.": {
      t: "fighting",
      id: "109"
    },
    "/:yeah.": {
      t: "yeah",
      id: "110"
    },
    "/:kiss.": {
      t: "kiss",
      id: "111"
    },
    "/:like.": {
      t: "like",
      id: "112"
    },
    "/:smug.": {
      t: "smug",
      id: "113"
    },
    "/:observe.": {
      t: "observe",
      id: "114"
    },
    "/:Broadcast.": {
      t: "Broadcast",
      id: "115"
    },
    "/:kaching.": {
      t: "kaching",
      id: "116"
    },
    "/:inspiration.": {
      t: "inspiration",
      id: "117"
    },
    "/:angel.": {
      t: "angel",
      id: "118"
    },
    "/:greet.": {
      t: "greet",
      id: "119"
    },
    "/:nosebleed.": {
      t: "nosebleed",
      id: "120"
    },
    "/:thinking.": {
      t: "thinking",
      id: "121"
    },
    "/:question.": {
      t: "question",
      id: "122"
    },
    "/:ask.": {
      t: "ask",
      id: "123"
    },
    "/:shush.": {
      t: "shush",
      id: "124"
    },
    "/:embarrassed.": {
      t: "embarrassed",
      id: "125"
    },
    "/:pitiful.": {
      t: "pitiful",
      id: "126"
    },
    "/:tear.": {
      t: "tear",
      id: "127"
    },
    "/:helpless.": {
      t: "helpless",
      id: "128"
    },
    "/:sweatsmile.": {
      t: "sweatsmile",
      id: "129"
    },
    "/:sleep.": {
      t: "sleep",
      id: "130"
    },
    "/:dizzy.": {
      t: "dizzy",
      id: "131"
    },
    "/:surrender.": {
      t: "surrender",
      id: "132"
    },
    "/:sorry.": {
      t: "sorry",
      id: "133"
    },
    "/:speechless.": {
      t: "speechless",
      id: "134"
    },
    "/:shocked.": {
      t: "shocked",
      id: "135"
    },
    "/:shutup.": {
      t: "shutup",
      id: "136"
    },
    "/:Boss.": {
      t: "Boss",
      id: "137"
    },
    "/:Beg.": {
      t: "Beg",
      id: "138"
    },
    "/:received.": {
      t: "received",
      id: "139"
    },
    "/:Busy.": {
      t: "Busy",
      id: "140"
    },
    "/:cute.": {
      t: "cute",
      id: "141"
    },
    "/:angry.": {
      t: "angry",
      id: "142"
    },
    "/:laughcry.": {
      t: "laughcry",
      id: "143"
    },
    "/:facecry.": {
      t: "facecry",
      id: "144"
    },
    "/:raisehand.": {
      t: "raisehand",
      id: "145"
    },
    "/:expect.": {
      t: "expect",
      id: "146"
    },
    "/:ok.": {
      t: "ok",
      id: "147"
    },
    "/:clap.": {
      t: "clap",
      id: "148"
    },
    "/:handshake.": {
      t: "handshake",
      id: "149"
    },
    "/:approve.": {
      t: "approve",
      id: "150"
    },
    "/:pray.": {
      t: "pray",
      id: "151"
    },
    "/:cheer.": {
      t: "cheer",
      id: "152"
    },
    "/:flowers.": {
      t: "flowers",
      id: "153"
    },
    "/:rose.": {
      t: "rose",
      id: "154"
    },
    "/:wither.": {
      t: "wither",
      id: "155"
    },
    "/:heart.": {
      t: "heart",
      id: "156"
    },
    "/:Brokenheart.": {
      t: "Brokenheart",
      id: "157"
    },
    "/:gift.": {
      t: "gift",
      id: "158"
    },
    "/:email.": {
      t: "email",
      id: "159"
    },
    "/:time.": {
      t: "time",
      id: "160"
    },
    "/:airplane.": {
      t: "airplane",
      id: "161"
    },
    "/:package.": {
      t: "package",
      id: "162"
    },
    "/:fire.": {
      t: "fire",
      id: "163"
    },
    "/:money.": {
      t: "money",
      id: "164"
    },
    "/:ship.": {
      t: "ship",
      id: "165"
    }
  };
  const isRichText = (content) => {
    if (!(typeof content === "string")) {
      return false;
    }
    return content && content.search(/<img|<strong/) > 0;
  };
  const replaceContent = (_content) => {
    let content = _content.toString();
    content = content.replace(/<img(.*?atmgateway-client.alibaba.com)/g, "<image$1");
    content = content.replace(/<img[^>]*>/gm, "[Image]");
    content = content.replace(/<(?!image|\/image|strong|\/strong).*?>/g, "");
    content = content.replace(/<image/, "<img");
    content = `<p>${content}</p>`;
    return {
      __html: content
    };
  };
  const formatContentOld = (content, imMessageType) => {
    let type = imMessageType;
    try {
      type = JSON.parse(content).cardType;
    } catch (error) {
      console.log("===== not card ====", imMessageType);
    }
    switch (type) {
      case 1:
        content = content.toString();
        if (content.match("<img src=")) {
          return `[${I18N.get("messenger.list.content.image") || "Image"}]`;
        }
        return content;
      case 2:
        return `[${I18N.get("messenger.list.content.image") || "Image"}]`;
      case 3:
      case 53:
      case 61:
        return `[${I18N.get("messenger.list.content.file") || "File"}]`;
      case 4:
        return `[${I18N.get("messenger.list.content.audio") || "Audio"}]`;
      case 5:
      case 62:
        return `[${I18N.get("messenger.list.content.video") || "Video"}]`;
      case 50:
      case 2e3:
      case 2008:
        return `[${I18N.get("messenger.list.content.message") || "Message"}]`;
      case 52:
        return `[${I18N.get("messenger.list.content.quotation") || "Quotation"}]`;
      case 54:
        return `[${I18N.get("messenger.list.content.product") || "Product"}]`;
      case 55:
        return `[${I18N.get("messenger.list.content.company") || "Company"}]`;
      case 56:
        return `[${I18N.get("messenger.list.content.behavior") || "Behavior"}]`;
      case 57:
        return `[${I18N.get("messenger.list.content.businessCard") || "Business card"}]`;
      case 58:
        return `[${I18N.get("messenger.list.content.ta") || "TA"}]`;
      case 59:
        return `[${I18N.get("messenger.list.content.tradeAssurance") || "Trade Assurance"}]`;
      case 60:
        return `[${I18N.get("messenger.list.content.image") || "Image"}]`;
      case 63:
        return `[${I18N.get("messenger.list.content.text") || "Text"}]`;
      case 64:
        return `[${I18N.get("messenger.list.content.orderTracking") || "Order Tracking"}]`;
      case 65:
        return `[${I18N.get("messenger.list.content.businessCard") || "Business card"}]`;
      case 66:
        return `[${I18N.get("messenger.list.content.businessCard") || "Business card"}]`;
      case 2001:
        return `[${I18N.get("messenger.list.content.quotation") || "Quotation"}]`;
      case 2002:
        return `[${I18N.get("messenger.list.content.ta") || "Order"}]`;
      case 9409:
        return `[${I18N.get("messenger.list.content.aiSummary") || "Summary"}]`;
      case 9999:
        return content.toString();
      default: {
        const defaultTag = I18N.get(`messenger.list.content.message.tag.${type}`);
        const defaultContent = I18N.get(`messenger.list.content.message.${type}`);
        if (defaultTag) {
          return `[${defaultTag}]${defaultContent}`;
        }
        return defaultContent || `[${I18N.get("messenger.list.content.message") || "Message"}]`;
      }
    }
  };
  const formatHtmlContent = (_content, imMessageType) => {
    let content;
    content = purify.sanitize(_content);
    if (isRichText(content) && content.startsWith("<p>")) {
      return replaceContent(content);
    }
    content = content.toString();
    content = content.replace(/\/n/g, "");
    const emotions = content.match(/\/:[^\/]+\.?/g) || [];
    if (emotions.length) {
      emotions.forEach(() => {
        for (const key2 in emotionData) {
          content = content.replace(
            `[${key2}]`,
            `<img width="32px" height="32px" src="//atmgateway-client.alibaba.com/smily-big/smile_${emotionData[key2].id}.png" />`
          );
          content = content.replace(
            key2,
            `<img width="32px" height="32px" src="//atmgateway-client.alibaba.com/smily-big/smile_${emotionData[key2].id}.png" />`
          );
        }
      });
      return { __html: `${content}` };
    }
    if ([1, 100015].includes(imMessageType) && content) {
      return replaceContent(content);
    }
    return null;
  };
  const MsgUtil = {
    formatContent(contentParam = "", imMessageType) {
      const content = decodeHTML(contentParam);
      const originContent = formatContentOld(content, imMessageType);
      const htmlContent = formatHtmlContent(content, imMessageType);
      return {
        content: originContent,
        htmlContent
      };
    }
  };
  function ListItem({ itemData }) {
    const {
      fullPortrait,
      name,
      loginId,
      accountId,
      accountIdEncrypt,
      unreadCount,
      chatToken,
      companyName,
      lastMsg = {}
    } = itemData;
    const { content, sendType, viewType, time: sendTime, msgType = 1 } = lastMsg;
    const finalName = name || loginId || accountId || "";
    const formatContent = (_content = "") => {
      if (viewType === 3) {
        return sendType === "send" ? I18N.get("messenger.youReverseTip") : I18N.get("messenger.reverseTip");
      } else {
        const { content: retContent, htmlContent } = MsgUtil.formatContent(_content, msgType);
        return htmlContent || retContent;
      }
    };
    const toMessenger = () => {
      goldlog("toMessenger");
      const messengerUrl = `${getMessengerUrl()}?activeAccountId=${accountId}&activeAccountIdEncrypt=${accountIdEncrypt}&chatToken=${chatToken}`;
      window.open(messengerUrl);
    };
    const formatedContent = formatContent(content);
    return /* @__PURE__ */ React.createElement("div", { className: "im-header-list-item", onClick: toMessenger }, /* @__PURE__ */ React.createElement("div", { className: "contact-left" }, fullPortrait ? /* @__PURE__ */ React.createElement("img", { src: fullPortrait }) : /* @__PURE__ */ React.createElement(
      "div",
      {
        className: "letter",
        style: {
          backgroundColor: getAvatarBackground(finalName)
        }
      },
      finalName.slice(0, 1)
    )), /* @__PURE__ */ React.createElement("div", { className: "contact-right" }, /* @__PURE__ */ React.createElement("div", { className: "contact-info" }, /* @__PURE__ */ React.createElement("span", { className: "name", title: finalName }, finalName), Number(sendTime) > 0 && /* @__PURE__ */ React.createElement("span", { className: "contact-time" }, timeSince(sendTime))), loginId !== BUYER_OFFICIAL_LOGIN_ID && companyName && /* @__PURE__ */ React.createElement("div", { className: "contact-company" }, companyName), formatedContent && /* @__PURE__ */ React.createElement("div", { className: "msg-wrapper" }, /* @__PURE__ */ React.createElement("div", { className: `latest-msg latest-msg-rec` }, typeof formatedContent !== "object" ? /* @__PURE__ */ React.createElement("p", { className: "latest-msg-oneline" }, /* @__PURE__ */ React.createElement("span", null, formatedContent)) : /* @__PURE__ */ React.createElement("div", { className: "latest-msg-oneline", dangerouslySetInnerHTML: formatedContent })))), /* @__PURE__ */ React.createElement("div", { className: "unread-count" }, unreadCount > 99 ? "99+" : unreadCount));
  }
  const login_url = `https://${PASSPORT_DOMAIN}/icbu_login.htm?return_url=${encodeURIComponent(
    window.location.href
  )}&scene=imHeaderNotification`;
  function List({ listData }) {
    return /* @__PURE__ */ React.createElement("div", { className: "im-header-list" }, /* @__PURE__ */ React.createElement("div", { className: "list-header" }, I18N.get("messenger.imHeader.message") || "Messages"), checkLogin() ? /* @__PURE__ */ React.createElement(React.Fragment, null, (listData == null ? void 0 : listData.length) ? listData.slice(0, 4).map((item) => /* @__PURE__ */ React.createElement(ListItem, { key: item.accounId, itemData: item })) : /* @__PURE__ */ React.createElement(React.Fragment, null, /* @__PURE__ */ React.createElement(
      "img",
      {
        src: "https://s.alicdn.com/@img/imgextra/i4/O1CN01lnw1WK1bGeXDIoBnB_!!6000000003438-2-tps-399-303.png",
        className: "no-data-img"
      }
    ), /* @__PURE__ */ React.createElement("div", { className: "no-data-tip" }, I18N.get("messenger.imHeader.noData") || "No messages")), /* @__PURE__ */ React.createElement("div", { className: "button-bar" }, /* @__PURE__ */ React.createElement("a", { target: "_blank", href: getMessengerUrl(), rel: "noreferrer" }, /* @__PURE__ */ React.createElement("button", { className: "list-view-more", onClick: () => goldlog("viewMore") }, I18N.get("messenger.imHeader.viewmore") || "View more")))) : /* @__PURE__ */ React.createElement(React.Fragment, null, /* @__PURE__ */ React.createElement("div", { className: "login-tip" }, I18N.get("messenger.imHeader.LoginTip") || "Sign in to view messages"), /* @__PURE__ */ React.createElement("div", { className: "button-bar" }, /* @__PURE__ */ React.createElement("a", { href: login_url, rel: "noreferrer" }, /* @__PURE__ */ React.createElement("button", { className: "list-view-more", onClick: () => goldlog("toLogin") }, I18N.get("messenger.imHeader.toLogin") || "To login")))));
  }
  function getUnreadInfo(data) {
    const { ctoken, pageId, params } = data;
    const url = `//${ONETALK_DOMAIN}/message/manager/unread.htm?ctoken=${encodeURIComponent(ctoken)}&dmtrack_pageid=${encodeURIComponent(pageId)}&params=${encodeURIComponent(JSON.stringify(params))}`;
    return fetch(url, {
      method: "GET",
      credentials: "include",
      headers: {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
      },
      mode: "cors",
      cache: "no-cache"
    }).then((response) => response.json());
  }
  const singleChatReg = /^\d+-\d+#11011(@icbu)?$/;
  function ImHeaderNotification() {
    const [listData, setListData] = React.useState([]);
    const [unreadCount, setUnreadCount] = React.useState(0);
    const cbSaver = React.useRef({});
    React.useEffect(() => {
      getUnreadInfo({
        ctoken: getCtoken(),
        // @ts-ignore
        pageId: window.dmtrack_pageid || "",
        params: {
          secAccountId: localStorage.getItem("sc-header-message-account-id") || "",
          needList: true
        }
      }).then((res) => {
        const { code, data } = res;
        if (code * 1 === 200 && (data == null ? void 0 : data.list)) {
          const list = data.list.filter(
            (item) => !item.mute && !item.block && singleChatReg.test(item.cid)
          );
          setListData(list);
        }
      });
      window.addEventListener(
        "message",
        (event) => {
          if (!/onetalk\.alibaba/gi.test(event.origin)) {
            return false;
          }
          let data;
          try {
            data = JSON.parse(event.data);
          } catch (e) {
            console.error("==== parse message error ====", e);
          }
          if (!data) return false;
          switch (data.type) {
            case "imUnreadCountChange":
              cbSaver.current.handleUnreadCountChange(data);
              break;
          }
        },
        false
      );
    }, []);
    cbSaver.current = {
      handleUnreadCountChange: (payload) => {
        setUnreadCount(payload.unreadCnt || 0);
      }
    };
    return /* @__PURE__ */ React.createElement("div", { className: "im-header-notification", "data-tnh-auto-exp": "message", "data-tnh-auto-clk": "message" }, unreadCount > 0 && /* @__PURE__ */ React.createElement("div", { className: "unread-count" }, unreadCount > 99 ? "99+" : unreadCount), /* @__PURE__ */ React.createElement("a", { target: "_blank", href: getMessengerUrl(), rel: "noreferrer", className: "action-icon" }, SVG_MAP.message), /* @__PURE__ */ React.createElement("div", { className: "balloon-wrapper" }, /* @__PURE__ */ React.createElement(List, { listData })));
  }
  window.ImHeaderNotification = ImHeaderNotification;
  exports2.ImHeaderNotification = ImHeaderNotification;
  exports2.default = ImHeaderNotification;
  Object.defineProperties(exports2, { __esModule: { value: true }, [Symbol.toStringTag]: { value: "Module" } });
});
