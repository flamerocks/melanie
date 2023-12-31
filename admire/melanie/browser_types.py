from __future__ import annotations

devices = {
    "iPad (gen 6)": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 768, "height": 1024},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad (gen 6) landscape": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 1024, "height": 768},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad (gen 7)": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 810, "height": 1080},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad (gen 7) landscape": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 1080, "height": 810},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad Mini": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 768, "height": 1024},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad Mini landscape": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 1024, "height": 768},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad Pro 11": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 834, "height": 1194},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPad Pro 11 landscape": {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 1194, "height": 834},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 6": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 375, "height": 667},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 6 landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 667, "height": 375},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 6 Plus": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 414, "height": 736},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 6 Plus landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 736, "height": 414},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 7": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 375, "height": 667},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 7 landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 667, "height": 375},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 7 Plus": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 414, "height": 736},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 7 Plus landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 736, "height": 414},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 8": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 375, "height": 667},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 8 landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 667, "height": 375},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 8 Plus": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 414, "height": 736},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 8 Plus landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 736, "height": 414},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone SE": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/16.0 Mobile/14E304 Safari/602.1",
        "viewport": {"width": 320, "height": 568},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone SE landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/16.0 Mobile/14E304 Safari/602.1",
        "viewport": {"width": 568, "height": 320},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone X": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 375, "height": 812},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone X landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/16.0 Mobile/15A372 Safari/604.1",
        "viewport": {"width": 812, "height": 375},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone XR": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 414, "height": 896},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone XR landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 896, "height": 414},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 11": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 414, "height": 715},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 11 landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 800, "height": 364},
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 11 Pro": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 375, "height": 635},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 11 Pro landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 724, "height": 325},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 11 Pro Max": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 414, "height": 715},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 11 Pro Max landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 808, "height": 364},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 390, "height": 664},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 750, "height": 340},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 Pro": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 390, "height": 664},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 Pro landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 750, "height": 340},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 Pro Max": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 428, "height": 746},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 Pro Max landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 832, "height": 378},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 Mini": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 375, "height": 629},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 12 Mini landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 712, "height": 325},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 390, "height": 664},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 750, "height": 342},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 Pro": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 390, "height": 664},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 Pro landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 750, "height": 342},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 Pro Max": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 428, "height": 746},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 Pro Max landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 832, "height": 380},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 Mini": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 375, "height": 629},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "iPhone 13 Mini landscape": {
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 712, "height": 327},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "webkit",
    },
    "Pixel 2": {
        "user_agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 411, "height": 731},
        "device_scale_factor": 2.625,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 2 landscape": {
        "user_agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 731, "height": 411},
        "device_scale_factor": 2.625,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 2 XL": {
        "user_agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 411, "height": 823},
        "device_scale_factor": 3.5,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 2 XL landscape": {
        "user_agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 823, "height": 411},
        "device_scale_factor": 3.5,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 3": {
        "user_agent": "Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 393, "height": 786},
        "device_scale_factor": 2.75,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 3 landscape": {
        "user_agent": "Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 786, "height": 393},
        "device_scale_factor": 2.75,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 4": {
        "user_agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 353, "height": 745},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 4 landscape": {
        "user_agent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 745, "height": 353},
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 4a (5G)": {
        "user_agent": "Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 412, "height": 765},
        "device_scale_factor": 2.63,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 4a (5G) landscape": {
        "user_agent": "Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 840, "height": 312},
        "device_scale_factor": 2.63,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 5": {
        "user_agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 393, "height": 727},
        "device_scale_factor": 2.75,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Pixel 5 landscape": {
        "user_agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36",
        "viewport": {"width": 802, "height": 293},
        "device_scale_factor": 2.75,
        "is_mobile": True,
        "has_touch": True,
        "default_browser_type": "chromium",
    },
    "Desktop Chrome HiDPI": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Safari/537.36",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 2,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "chromium",
    },
    "Desktop Edge HiDPI": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Safari/537.36 Edg/108.0.5359.22",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 2,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "chromium",
    },
    "Desktop Firefox HiDPI": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 2,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "firefox",
    },
    "Desktop Safari": {
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 2,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "webkit",
    },
    "Desktop Chrome": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Safari/537.36",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 1,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "chromium",
    },
    "Desktop Edge": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Safari/537.36 Edg/108.0.5359.22",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 1,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "chromium",
    },
    "Desktop Firefox": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "viewport": {"width": 1280, "height": 720},
        "device_scale_factor": 1,
        "is_mobile": False,
        "has_touch": False,
        "default_browser_type": "firefox",
    },
}
