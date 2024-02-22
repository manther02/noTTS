"""No TTS service."""
import logging

import base64
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
import homeassistant.helpers.config_validation as cv

CONF_BEEP = "beep"

_LOGGER = logging.getLogger(__name__)

SUPPORTED_LANGUAGES = ["pt", "en", "es", "fr"]

DEFAULT_LANG = "en"
DEFAULT_BEEP = "0"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORTED_LANGUAGES),
        vol.Optional(CONF_BEEP, default=DEFAULT_BEEP): cv.string
    }
)

BEEP = "UklGRspTAABXQVZFZm10IBAAAAABAAIAgD4AAAB9AAACAAgATElTVBoAAABJTkZPSVNGVA0AAABMYXZmNjAuMy4xMDAAAGRhdGGEUwAAgICAgICAgICAgICAgH+AgICAgICAgICAgICAgICAgH+AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIB/gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAf4CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIB/gICAgICAgIB/gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAf4CAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAf4CAgICAgICAgICAgICAgICAgICAgICAgICAf4B/gICAgIB/gICAgIB/gH+AgICAf4CAgH9/f3+AgICAgH+AgH+AgICAgIB/gICAgH+Af4B/gH+Af4B/gICAgICAgICAgH+Af4B/gH+AgICAgH+AgIB/gH9/gH+AgIB/gH+Af4CAgH+Af4CAgICAf4B/f4B/gH9/gH+Af4CAgH+Af3+Af4B/gH+Af4B/gH+Af3+AgIB/gH+Af39/gH+AgICAf39/f39/f39/f4B/gH9/gICAgIB/gH+AgIB/gH+Af4B/gH9/f3+AgICAgICAgIB/f4CAgH9/f4B/f4B/gH9/gH+Af4B/gH+Af4B/gH+Af3+Af4B/gH9/f4CAf4B/gH+Af4B/gH+AgICAf4CAgICAf39/gH9/f3+Af3+AgH+Af4CAgIB/gICAgIB/gH+Af39/f39/gICAgIB/gICAgIB/gH9/gH+Af39/f39/f3+AgH+Af3+Af4CAgICAgIB/f4CAf4CAf39/gICAf39/gICAgICAgIB/gICAgICAgH9/f39/gH9/f39/f39/gH+Af3+AgH+AgH+Af4B/f3+AgH+Af4B/gH+Af4B/gICAgICAgIB/gIB/f39/f4B/gH+Af4B/gH+Af4B/gH9/gH+Af4B/gH+AgICAf4B/gH+Af4B/f39/gH+Af4B/gH+AgICAf4B/f39/f3+Af4CAf4CAgICAf4CAgH+Af4B/gH9/gIB/gH9/gH+AgIB/gH+AgICAgICAf39/gH9/f39/gICAf4B/gH9/gH+Af4B/gH+Af4B/f4CAgH+Af4B/gH+Af4B/gICAgH9/f3+Af4B/gH9/f4B/gIB/gICAgH+AgH+Af4CAgH+Af4B/gH9/gH9/gH+AgH9/f4B/gH+Af4B/gICAgICAf4B/gH+Af4B/gH9/f4B/gH9/gICAgH+AgIB/gIB/gH9/f4B/f4B/gH+Af4B/gH9/f39/gH9/f39/gH9/gH+AgIB/gICAf4B/gH+Af3+Af4B/f4B/f39/f39/f4CAgICAgICAgICAgH+Af4CAf4B/gH+AgH+AgICAgICAgIB/gH+Af39/f3+Af4B/gH+Af4B/gH9/gH+Af4B/gH+AgICAf4B/gH+AgH+Af3+AgH+AgH9/gH+Af4B/gH+Af4B/gICAf4CAgIB/gH+Af39/gH9/gH9/f39/gH+Af4B/gH+AgH+Af4B/gH+Af4B/gH+Af3+Af4B/gH9/f4B/gH+AgICAgICAgICAgICAf4B/gH+AgH9/gH9/gIB/gH+AgH+Af3+AgICAgH+Af3+Af4CAf4B/gH+AgICAgICAgICAgH+AgIB/f4B/gICAgH+Af39/f39/f4CAf39/gH+Af39/f4B/f4CAgH+Af4CAf4CAgICAgH+AgIB/gIB/gH9/f39/f4B/gH+Af4CAf4B/gH+AgICAgICAgICAgICAgICAf4B/f39/f3+Af4B/gICAgIB/gH9/f4B/gH+AgICAgIB/gH+AgICAgH+Af4B/gIB/gH+Af4B/f39/f3+Af4B/gICAf4B/gH9/f39/f4B/gH+BgIOChIOEg4SDhIKCgYB/fn17e3l6d3l2eXZ5d3l4enl7fH5/gYOEhoeJiYyLj42SjpWPlo6TioyEg314dWttXWVSX09gVmdmdHyFmJq3rs+82L7Ps7acjHhTTh8vDCQMLhpDOVxZdnuOmqK2s8y+2cPcwNW4x6qymZqGfnFiXElLNT8oOSM7J0IxTkFdVG5qgYOSm6CxrMK0zLbNs8esuqGok5OCe3BkXlBRQUk4SDdMPFVIYVdvaX5+jZSbqae7sMe1y7XJsMCnsZuei4l6cmleW05RQ00+TkBTR11UamN5dYiJlp6isKy+ssa0x7DBqbWdpZCRgHxvZ2BVVEhNQU1AUUVZT2Vdcm2Bf5CTnaanta6/scOwwaq4oaqUmIWEdXBmXVlOUERMQE5CVEpfVmxlenaJiZecoq6quq7ArsCquaKsmJuLiHx0bGJeU1RITkNOQ1NKXFRnYXVwg4GQkpujpLCquay8qrmlsJyhkZCDfXRqZVlYTE5FS0RNSFVQYFxuan16jIqZmqSoq7Kut623qLGgp5WYh4d4dWlkW1VQTEtITElRTltXaGN3cIaAlJCgn6mrrbSut6u1pK6Zoo2SfoBvbWBdVU9OR0xEUEdZT2Vbc2uCfZCRnKKlsKu4rLuquKSwnKORkoSAdm5oXlxRU0pPSFBLVlJgXW1qe3mJiZaYoKaosau3rLiotKGql5uLin54b2dhWFZOT0lOSlJPW1lmZHRxg4CRj5yepaqqs6u2qbSkrZuikZKEgXZvZ2BbVFJNT0pQTVdUYV5uan14i4eYlqGjqK6qtKq1prCfp5WZiol8eG5nYFpVUE9MT0xTUVxaaGV2coWAk4+enaapq7Crs6ixoqqZno6PgX9zbmVfWlVSTk9NUVBYWGNicG1/e42JmZeio6irqq+pr6SqnaCTlIeGenhsa19fVldRUlBSVFZdXmhod3OGgJSNn5mnpKusrK+orqKnmZyOjoB/cnBjY1daT1VMU05WVltiZHJvgnuSiJ+VqaCuqa+uq66kqpqgjZN/hHB0Y2dYXVNXUlRWVl1bZ2NybH93jIKYjaGZpqOoqqatoKuZo5CZhox8fnBxZWVcXFdWVVRYVl9caWV2cIR8kYmclaSgqKeoq6SrnqeWno2Sg4R3dmtpYF5YVlRTVFVZWmJibm19eIuFmJGinKelqamnq6GpmaKPmYWMen5vcGVjXFpXVVZVWFlfX2pod3KEfZGJmpWhn6SmpKqiqp2llpyNkIKCdnVqaF9fV1hUVlZXXFxmZHNsgHeNhJeQnpqio6OooamdppefkJWHiXx8cXBlZVxdVllVWFhbYGFraXlyhnyTiJyUop2kpKSnoaebopOaipCAhXR5aW1gY1ldV1lYWV1dZmRybYB3jYKYjaCXpKCmpaSnnqWXno6VhIp5fm5yZGddYFlcWVtdXWNibWl4coV8kYeakqCbo6KjpaClmqGTmImOf4NzeGluYGZaYFhdWV1fYGhmdG2Cdo6BmIyflaOdo6KhpJyilZyNlIOKeX9vc2ZpX2JaXlldXGBkZG5re3SHfZKHm5GhmaSeo6GfoZiekJiHj32Ecnlpb2FoXWNcYF5gZGNsaHZvgXiLgJSIm5Cfl6Ccn56bnpWajpOEjHqDb3pncWFqXWVdYmBiZWRuaHhvg3iOgZeLn5OimaOcoJ2am5OWiY9/iHR/a3Zjbl5pXGVcY2BkZ2Zwa3xxiHmSgpqLn5OinKOioaedp5aijpaDhnVwZVlVRkg+QUREVlBxZpKDs6PEu7vDobuAqWOTUH9Mb1RlZGB4YY1moW+vebWEs42pkZiSgo9piFGAQHk4cjtvSm5fcXh4lICti8CVyZ3Jn7+dq5SRiHF4UWk3WydTJE8uUkFbWmh3eJaLsp3Fq860zbbCsa+llJR2f1lqQlc2SjVEPkVPTmRbe22TgaiVt6a+sry3sbSgq4uddY1ifFZsU19WV19Ua1d6X4lql3iihqiSp5yfoJKggZtwkmKJWoBaeGBybHB7cI1ynXipf6+Fr4qnjJmMhohxglx7THRFcEduUm9jc3d6jYOhjLKVvZzBoL2fsJqckIODaXRQZUBaOVQ8VEhaWmNwcIh/npCxn76rwbG8sa6rm5+Dj2x8WGpLWkZQSUtSTmFWc2OFc5aFpJaso6yrpa6YqoehdpVnhl92XGhgXmdZcVt8YYdqkHWXgJqKl5KQl4aXeZNtjWSGX39feWV1b3N7dIl3lnyigaiGqYmji5iKh4Zzf2B4UnBLaktoUmlebm52f4GRjKGVrp23obqhtJ2nlJOIenhiaE5bQ1NAUEVUUV5hbHV8i42fnK+oua+7sbSspqKUk3+CbHBdX1RUUE5ST1pVZmF1b4Z/lpCinainp6yfqpOihZd3iW17Z25lZGdgbGB0ZH5rinOUfZuFnY2Zko+TgpF0jGeGX39deWB2aHZyeH99joGchqeJrYusi6OJlIWBfmx3W3BPaktmTmdXbGN1cn+Di5SWpZ6yoriitp6tlp2LiX5yb15iT1dIUkdTTVpZZmh1e4WPlaGirqy0sLGuqKabmYuJendsZWJYW1FZUFtVYV9rbHl6h4iVlp6goaadp5Wjipp/jnZ/cHBtZW1gb190Y3trg3SMfZOGlo6Uk46WhJR4jm2GZn1jdWRvaW1wbntzh3qUgaCJqI6qkqaUnJKNjXuFaXpbblJjUF1SXlplZXB0f4WNl5mmorKltqWyoKeWl4qEenFpYVtWUVFPUFRVX19ubX9+j46dnaenrKqsp6agnJWOiH17bHBeZlVgU19YYWJpbnN7gIiMlJWdmaOXpZChhpl9jXV/cXFvZ3Bhc2F4ZX9thneOgZSKlpGUlY6WhJR4j22HZH1gdGBtZWttbXdyhHmSgZ6Ip46sk6qVopSUj4KHcHxgcVRmTmBOX1NjXmxseH2GkJKinLCiuKS4oa+aoJCNgnlyZ2NZWFFTT1RTXF1paXd5homTmJ6ipqeppqegn5WSiYN9cnNka1plVmRZZmFrbHN4foSJj5KYl56XoZOgjJiDjXp+c3BvZm1hbmFxZndvfnmHg5CLlpKZlpiYkZeHkXyIcXxpcGRnYmJkY2lqcXN8fomJlZKfmaScpJyel5SPhoR4dmtpYF9aWldcWWNhb2x8fIqOlp+fqqOupKufopaUioV7dWxpX19YW1ZbW19lZ3Fyf3+NjJiXoZ6moKadoZWXjIqDenpqc15uV2pYaV9ranB3d4WBkIuZkp+VoJOdjZaFi31+dnJzaHJic2J1Z3hvfHmBg4aMi5SOmY+ajZiHkoCJeH1xcWtnaGJoYmtncG94eoOFjpCYmZ+eoJ+cnZOWiIp7fG9sZV9eV1tXXV1iaGp3doaFk5OeoKSopaqipZqcjo+AgHByYmVYXVRYV1hhXG5lfXKLgJmPopuoo6iloqKXmomQeIZpe1xyVmtXZ15maWh3boV2kX+aiKCOoZGfkJiNjYmBhHR/aHtheF93YndqeXR8gICKhZOLmo6dj5uMloaNfoF3dXFqbmJtYG5jcmp3dH+AiYuSlZqbnZ6cnJaWjI2BgXZ0bGhlX2FcYF5jZWpwdH2Aio2VmZ6ioqahpJyckpKGhXh4am1fZVlgWV5fYGlmd2+FfJKInZOjm6SeoZyYl4yPfodwfmR3XHBZal1oZWhxbH5yi3uWhJ6Mo5Gik52SlI2Ih3qBbXtidlxyXHFgcmp1dnqEgJCHmoyfjqGMnYeWgYt7f3Zyc2hxYXFgcmR1a3p2gYKJjpGXlpyXnZWZj5GGh3x8cnFqaGRiYWJiZmdub3p6hoaRk5mcnqKeo5mekZWGinp+bnNkaV1iW15gXmlidmqEdZKCnY+jmqShoKKYnYyWf4xzgmd4X29baFxlYmRsZ3luh3eTgpyLopGjk5+Sl4+Lin6FcYBme153W3VedGV2cXp/f4yFlomdip+JnISWf415gnV2cmxxZXJhdWJ4aH1wg3yLiJKSmJmZnJabjpaEjXmCb3Zoa2NjYmBjYmhpcXR8gIiMlZaenKOdo5qelJSKiYB9dnJsaWVjYWBiX2hjcWl9c4p/lYudlqCen6GZoI+bhJN5iW5/ZXRfal5kYWFqY3VpgnKPfZqGoI2ikp+TmJOOkoOOdolrgmJ6XnReb2RubnB7dYh8k4Saip2NnIyYiJCDhn57enB3Z3VidWF2ZXhtfHiBhIePjJeQm5Gbj5eLkIWHf3x4cnJpbGNpYWhlbGxyd3yEh4+RmJicnJybl5eQkIeIfX90dmttZGVgXWBZZFtsY3lziImZoqm3ssGzvKiolId3XVg7QS86QUhpZZaHuKPCsriynqZ9k1x+RG05Yj9hVGdzcZZ+torLk8+Ww5OqjImCZ3hKcDlrNWxBclp9e4yfmb2jz6bQoMGUpoOEcWJiR1k5WDpdSWpie4KOop66qMWpv6Gsko9/bmtPXDpUNFU8XVFsbn+Pkq+ixKvJqr+gqY+Le2lnS1c3TjBON1dLZ2d7iJCnorysw628pamYjodxdVhlR1lCVElXWmBxb4qAoI+umrCfpp2Uln2LZn9TdEpsTGlaam9wiXiigbSIuoyzi6CHh4JrfFJ3QnQ+c0d1Wnl0gZKJrY++ksGQtoqhgoV5aHJSbkZtR29SdGV9foeYkK2VuJa2kaiIkXx1cltqSGdAakVxVnxwiY+Vrp3Dn8mawZCsg492b2tSYz5gN2E9aE9zaIKHkqWfu6bFpsCesJKXg3x0YmdQX0dcSmBXamx3hIabkqqar5yqmJuQh4dxfV51U3BTbV1vbnWDfZqEq4uzja6NoImKhHJ9XHhPc01xVnJmdnp9kIWji66OsI+ojJeGgoBselp1UHJQcll0anmAf5iEq4i2ibSIpoWPgHV8XXhMd0d3THpafm+Dh4mfjrKPu424h6p+lHZ5bl9oTGdCakRxUXtmh4CTnJuwn7qct5SoiZJ9eXJjaFNjTWJRZ15xcX2IiZyTqZitmKWTlYyBhGx7XXRUb1RtXHBrdoB9lYWni6+OrI6fi4yFdn5ieFN0TXJRc152cXuHgZ2Hq4uvjqiOmYuFhnCAXnlTdVFyWnNpdn58lIKmh7CKroqiho+Cd3xheFF1SnVMd1l7bYGHh6CMs4+7jrWKpYOOe3VzXm1Pa0hrTHBaeG6Ch4ufk7CXtpevkp+Ji390dmJuVmtSa1hvZnZ5f46HoY2rkKyPooySh36Aa3pcdFRxVXJfdXB7hIOaiqqQsZKtkZ+MjIN2eWNwVWpQaVRtYXR1fYuGn42ska+Sp5CXioSEcHxfdVVxVHFcc2x4gX6XhKiIsYquiKGEjH51eGBzUXBLcU91XXxyg4uLopCzkriRsouig4x6dXFfalBoSWpNcFl4bYKGi5ySrJWxlKyQnomLgHV3Y3BXbVNuWXNmenmBjoeejKeNp4ydiI6BfHpqc1xvVG9Wc2B7coSHjJuTqpevlqqRnImJfnR0YGxTZ05nU2tgcnN7iYWdjqmVrZiml5mSh4l0f2R2WXBWb11xa3V8eo+AnYWkiKOJmoiLhHqAanteeFl4W3pmfneDi4idi6mNq4ykiJWBgnpvc15tVGxSblh0Znx5hY6NoZOslq6Vpo+Yh4V9cXNgbVdrVW5ddGt8foOSiqCOp4+kjJqGi395d2hwXG1Xb1p0ZXx3hIuMnZGolKuTpI6Yhod8dHJia1ZnUmhXbWR1dn6Kh5yPqJSrl6WVmY+JhnZ8ZXRablVtWm9mc3d6ioCZhqOLpI2ejJKIgYJwe2J2W3RddmZ5dX+GhJaIoYukjJ+JlISFfnV2ZnFcbllvXXNpeXqAjYedjaeQqJCgjZKHgX9ueF9zWHFYc2J3cnyEgZWFooiniqOKmIaIgXZ5ZXNZb1ZvW3VpfXuHj4+glaqWq5OkjJWBgnZtbFxmUWVQaVlwaXp+hJOOo5Wtmq2apZaWjYOCb3ZebVVoVWdda2xyfnuQg56LpZClkp2QkIp+gm16X3NZcFxxZnV2fIiCmImijaWPoY2XiYiCd3pnc1xuWGxdb2l1eX2KhpiOoJShlpuTkIyCgnN5Z3FgbmFuaHJ0d4J+j4SYiZuMl42OiYKEdH1pdmJzYXNod3R9g4SRi52QopGgkJiLi4N6emlxXGpVZ1dpYG9veIKDk42glaeZppmelZGNgYNweGJvWmlbZ2NpcG+Ad5CBm4qgkZ2UlZOHjneFaXxhdF9wZm9xcoB3jX6XhZyLnI6WjY2KgINze2hzYW5hbWdwcnZ+fouFlYybkJyRl46OiYKCdXprdGZwZ3Btc3d4gn6MhJOIloqUiY2GgoF2fGt3ZXRmdG14eX6GhJOLnI+fkZyPkoqEgnR5ZnBcaltnYGhsb3t5i4SYj6CXo5ufmpaUiop7f210Y2xfaGJpam51doF/jYiVj5qTmpKVjouGf35xdWdvYm1lcG12en6Hh5OOmpOclJeRjoqBgnR4am9kaWVoamt0cn97iYSRjZaTl5aUlIyQgYl2gGx3aHBpbG5sd3GBeIuAkoaVipOMjIuCh3eBbntpdmp0cHV5eoOBjYiUjpePlo2Qhod+e3Zvb2ZrY2plbm51en6IiJOQm5ael5qUkY2EhHd7a3Jka2Rpamp0cIB4jIKUipmQmJKTj4qKfoNye2lzZm5obG9veXaFgJCJmJGblZmVkZGHinqBb3dobWZmaGRvZ3dvgXqKhpCRlJiTm4+ZiZKBiXp+dXNya3JodGp4cH15goKFiYiMiIyGioGGfIJ4fXZ5d3Z7d4B6hn+KhY2KjIyJjISIfYN1fnB3bHFsbm9tdnF+eIaCjYuSkpOVkJSLjoOFe3x0c3BscGlybHZzfH2BiIaRiJaIloaRgop+gHl2d213ZnllfWmCc4d/i4yNl42cipuFln6Od4RxeW1tbmVxYXdkfm2GeIyFkZCTlpKYjpeIkoGKe4F2d3Nvc2p0a3dwe3h/gIOIhYyFjoSNgomAhIB9gHeBc4NyhXaGfIaDhYiDi4GLfYl5hXaAdHp0dHVveW5+cYR5ioGOiY+Ojo+KjIWHf4F6end1dnB2b3hye3h+gIGIhI6FkIWOg4mBgn57fHV7bnxqfWp/b4F3hIKGjYeVh5iGl4OSf4p6gHZ2c2xyZXRjeGZ+b4V7ioeMkIyWi5eHlYOQf4h6fnd0dW11andse3J/e4GEgoqCjYGNgIuAh4CCgXyCdoNyhHKFdoR8g4OBiH6Le4t4inaHdoR2f3h5e3WAc4V0iniMfY2DioaGiICIfIZ4g3aAdXx3eXl2fXiBfISChomGjoSOgoqAhH59fHd7cXxtfmyBboR0hn6HiYaThZmCmn+XfI95hnd7dXB1Z3die2KBaIdzjICQjI+Ui5iEmH6TeIx1hHR7dHJ3bXxsgW+Gdol+ioWIioSLgIp8h3mDd394enp2f3OEdIl3jH2Mg4iJgox7jXaMdIl0hHZ+end+coNvhnCIdIh6hoGDhoCJfop8iXuHe4R7gHx8f3qCeoV9h4CGhIOGfoV6gnh+eHp5dnx0gHKEc4h2i32MhYqNh5SBl3qVdZByiHJ+dHV4bH1ngmWIaIxwjnqOhYqOhJR+l3mVdpF0inSCdnp5cn5ug26HcYp4in+HhYKJfYp5iXeHd4N5fnx6f3aCdYZ3iHuJgYaGgop8jHiLdoh2hHh+enl+dIJxhXKIdYl6iICFhYKJfot6iniHeIN4fnp5fHeAeIV7iYCKhYiIg4h9hniCdX12eHh0fHGAcYV0iHmKgYuJiI+ElH6VeJJ0jXKEc3x3c3tsgGiFaYptjXWOfYuGho2AkXqSdZFzjHKGdIB4eX10gnKIc4x3jXyLgYaFf4d6h3eGdYN2f3h7fHiAdoR2iHqKfomDhoiCin2LeYl3hniBen1+eIJ0hXOHdId3hXuCf36De4Z5iHiIeoZ8g3+Agn2FfIh8iX+JgoeEgoV8hHeBc31zeXV1eXN9coN0h3mLf42GjI2JkISRfY93i3OFcn5zd3Zxe26BbYdvjHSPe46Ci4iEjX2Pd45zi3GGcoF2fHt4gXaHdot5jn2NgYqEhIV+hXiDdIFzfXV6eXh+eIR5iH2KgoqGiIqDi36KeYd2g3Z+eHp7eIB3g3eGeYh7h36GgYOCf4N7g3iDeIN5gXuAf3+DfoWAh4KHhYeGhIWBg31+eXp2d3Z0d3R6dX94hHyJgYyGjYyLj4aQgI55iXSEcn5yeHV0enCAb4Zxi3WNfI2CiYiEi32Md4p0iHKDdH94e354hHiJeY18jX+LgoaEgIR6g3aBc39zfHZ6enh/eIN5hnyIgIeEhoeDiICHfYV6g3iBd394fXt7fnqCeoR6hnyGfoV/goB/gH2Aen95gHqAfIF/goODhYSFhoSHgoeAhH2Ae3x6d3l0eXJ7cn50gniFfoeFh4uGkIORgY9/in2Een54eXd1eHJ6cn50g3iGfYiDiIiGioOJgIZ8gnh+dnt1eXh5fXqCfYeBiYWKiIiJhYiBhX2AeHx1eHN1dXR5dH93hHuIgYqHiouIjoaNgop9hXiAdXtzeHV2enV/d4R6iH6JgoiFh4WFg4KBf357fHl7eHt5fXyAgISDh4WKhYuFioWGg4CBen50e294bnlve3R/eoKChYqGkYWUhZSEkIKJf4F8eHlyeG55bnxwgXWEfIaEh4uGj4WPg4yAhnx/eXl3dXhze3WAeYR/hoWGioWNhIyCiYCDfX16eHl0eXN7c392gnqFf4aEhYiEi4OMgYt/iXuEeIB1e3Z5eXd+doR4iHqJfoiBh4OFhIODgIF7f3d9dHx0fneAe4OAhYOHhIiFh4aFhYGEfYJ4f3N7cXlxeHR5eXx/f4WAi4KOg4+EjoWJhYSCfX93fHN6cXlye3V8en5/f4OAh4KJhIqGh4aChH2AeXx4enh6ent+fYF+hH+HgImBiYKHgoKBfX93fnN9cn5zgXaDeoSAhIWCioGOf49+jnyJe4N5fHl3eXR8c391gneFe4aAiISIh4iIhoeCg31/eHt0enN6dX15gH2CgYWFhoiHioaLhImAhnuBd3tzeHN2dnZ6eX97hH+IgoqGjImLiomJhIV/gHp7d3h1dnV2eHd7eX58goCFhYiJiIyGjIKKfYV5gHd7eHh6dn51gnWFeId7iYCJhYeIg4l9iHeFc4JxfnN8d3t9eoJ7h3yLfo2BjYOKhIWDf4F5f3Z9dXx3fHl9fX6AgIKDhIaFh4aGhIOBf356e3d6dnp2fXl/fYKBhIaFioaMhoyFiYKEfn56eHZ0dHJ0dHd3e3yAgYSGiIqMjY2NjIuIhoKBfHt4dnZzdnN3dXl4e31+g4GIhIuGjIaLhIeBg35+fHp8d312fneAeYJ8hICFg4aGhoeDh3+FeoJ1f3N9c3t2ent6gHuFfYl/jIGMgoqDhoOAgnuBd4B1f3Z+eH58fn9/gn+EgIWAhX+DfoB9fHx6fHl8en19f4CCg4SFhYeGh4aHhIWBgn59enl3dnZ1d3Z6eH17gH+Dg4aGiImJioiJhYeCg35/enx3enZ5d3p6e319gH+CgYWChoOGg4aChICBfn99fHx7fXp+eoB8gn6FgYeDh4SGhIOCf4F6f3d+dX52fnh+e35/f4J/hoCJgIqBioGHgoOCf4F7gHl/eH55fnt+fX6Af4F/goCDgIJ/gH9/f32AfYB+gH+BgYGCgoKDg4KDgYN/g3yBe396fHt6fHl9eX97gX2DgISChYSGhYWGg4WBg36BfH96fXh8eHx5fHt8fn2Bf4OAhYGGgYaBhYCCfoB+fn18fnt/e4B8gX6CgIOBg4KDgoKBgIF9gHt/eX54fnl+en59foB+g3+GgIeCh4OGg4ODgYJ+gXyAe396fnt9fHx9fX99gX6Cf4OAgoGBgoCCf4J+gn6Bf4F/gYCAgYCCgIN/g36CfoF9f319fXt+e358f32AfoF/goGEgoWChYOFg4SCgYF/gHx/eX93fnd+eH57fn5+gn6Gf4h/iX+If4V/gn9/gHuAeYF3gXiCeYJ9goCChIKGgId+hnyDe4B6fXt7fHp+eoB7gn2EgISChYSEhIOEgYOAgX5/fH57fHt7e3p7e3x8fn6AgIKDhISEhYSFg4OBgYB/f31+fH18fHx8fX1+foB/gYCBgYGCgIJ/gX2BfYB9f39/gX6DfoR+hn6Gf4V/goB/gXyCeYJ4gneCeIJ6gX2AgX6EfYZ8h3uHfIV8gn5/gH2Ce4N6hHqEe4N9gn+BgYCDf4R/g36CfIB7fnp8ent8e358gX+DgYWEhoaGhoWFg4SBgX9+fHx7enp5enl7enx8fn6AgIGCg4SDhoOGgoaBhICCf4B+fn19fHx9fH59f36Bf4KAg4CDf4J/gX5/fn5+fX98gXyCfIR9hH6Ff4SAg4GBgX6CfIJ6gnmCeYJ6gXyAfn6BfYN8hXyGfIZ+hoCEgYOCgIJ+gnuBen95fnp+e35+f4CAgoGEgYSBg4GBgICAfn99fXx9fX1+fYB/goGEgoWEhISCg4CCfoB7fnl9eHx4fHp8fH1/foKAhYGHgoeDhoOEgoKBf4B9fnt9enx6fHp9e359f36BgIKBg4KEgoSCg4GBgH5/fH96gHmAeYF7gX2BgICDgIV/hn6GfoR8gnuAe358fH17f3qBe4N8g36EgISBg4KCgoGCf4J+gX2AfH97f3t/fH99f35/gH+Cf4N/hH+Df4J/gIB/gH+Af4CAgIGAgYCBgIGAgIB/f35+fH57fXt9e318fn5/gIGCgoSDhYOGg4aBhYCDfoF9fnx7fHl9eX56f3yAfoGAgoGCgoKCgoKBgYCAf4B+gHyAfIF8gX2CfoJ/goCCgoGDf4R9hXuFeYR4gnl/e3x+eoF5hHmGeod8h36HgYaDhISBhH2DeoF4gHd+d315fXt9fn6Bf4R/hoCHgIaAhH+Bf39/fX98f3x/fn9/gIF/goCCgIKAgYB/gH2Ae396fnt9fH1+foF/g4GFgoaCh4KGgYSAgX5+fXt7ent5e3p9fH9+goCEgoWDhoSFhISDgYF/gHx+en16fXp+e398gH6CgIOChISDhYGGf4V8g3qBeX95fXt7fXqAeoR7h3yJfoqAiIKFhICEe4R3g3WBdX93fXp8fnyCfIV9h36IgIeBhIKAgnyCeYJ4gXiAen59foF9hH2GfYd9hn6EgICBfYF6gXmBeYF6gHyAfoCAgIOAhH+Gf4Z/hX+Df4B+fn18fXt8e317f3yBfYOAhYKFg4WEhIOCgYCAfX56fXl9eX55gHuCfYOAhIKEhYOGgYZ+hnuEeYJ5f3l8e3p+eYF6hHuHfYh/iYKHhISFgIV8hHqCeIB4fnp8fHt/e4F8hH6Ff4aBhYKDg4CDfoN8gXuAfH98fn59gH2BfYN+hH+Ef4OAgoGAgX+BfYB8f3x/e358f35/gICDgYWBhYGEgYJ/gH5+fHx7fHp7e3x9fYB/g4GFhIaFhoWFhIOBgH59fHp6eHp2e3d9eYB8gn+Fg4aFhoeFh4KGf4R8gXp/eXx5e3t6fXuAfIN9hX+HgIaChYODg4CCfYF7gHl+eX15fXt9fX2BfoR/hoCGgYWChIKBgX6BfH97f3t+fH5+foB/gX+Cf4KAgYCAgH+AfoB9gH2AfYB+gX+BgIGBgYKBg4CDf4J+gn2AfX98fXt8e3x8fH59gH6DgIaCh4OHg4aDg4GAgH1+en14fHh8eX17f36BgYKDg4WEhoOGgYV/gn1/fHx6enp5e3p9e39+gYCEg4WFhoWFhYSEgYF/fnx8enp5eXl5ent8fn+AgYOEhYWGhYaEhYKDgIF+fnx8fHt9en57f3yBfoOAhIGDgoKCgYJ+gXyAe397f3x/fYB/goGDgoOEgoSAg36CfIF6f3l9eXx6fHx8gH2DfoaAiIKIg4aEhISAgn2Aen54fHd7eHt6fH1+gICDgoWEhoWGhYWDg4GBfn58fHp6eXl6enx7fn6BgYSDhYWGhoaFhIOCgX9+fHt6enl5enp7fH1/gIGCg4SEhYSFhISEg4KBgH9/fX18fHx8fHx9fX9+gX+CgIOAhIGDgYGBf4F9gXyBe4J7gnyCfoGBgIN/hH6FfIR8gnt/e318e316f3uBfIR+hoGHg4aFhIWChH+CfIB6fXh7eHp5ent7fn2Cf4WCh4WHhoaHhIWBg35/e3x5enl5eXl7e359gYCDg4WGhoeGh4SGgYN+gHx8eXp4eHh4eXl8fH9/goOFhoaHhoeFhYOCgX9/fH17e3p7e3t8fH59gX6Df4WAhYCEgYOBgIF9gXuBeYF5gXqBfIF/gYKAhX6GfYZ8hXyCe4B8fXx6fXl/eYF6g32EgIWDhYWEhoKFgIN+f3t8enp5eXl5e3t9fYCAg4SFh4aIhoeEhYKBf358enp3enZ6d3x5f32CgYWEhoeGiYWIg4aAg36Ae315enl4eXh7eX17gH+DgoWFh4aHhoaEhYKCf4B8fXt6enl6eXx6fnyBfoSAhoKHg4aDhIOBgn2Be4F5gHl/e399gH+AgYCDgIR/hH6EfYJ8gXt/fH19fH99gX6EgIWBhoOGg4SDgoJ/gHx+e3x6enl6ent8fX6AgYODhYSHhYeEhoOEgYB/fX16e3h7eHt4fHt+foCBg4SEhoWHhIaDhIGBfn98fHt6enp6enp8fH9/gYGDg4SFhIaDhYGEf4N9gXt+enx6ent6fXqAe4J9hH+FgYWDhISChICDfoJ8gXt/en97fn1+fn+Af4J/g3+Df4N+gn6BfX99fn59f32AfoKAg4GEgoSChIGCgIB+fn18fHp7ent6fXt+fYCAgoKEhIWGhYaEhYKDgIB+fXt7enp5enp8e35+gICCg4SFhYaEhoOEgYF/fn17e3l6eHp5e3x9fn+BgYOEhYWFhoSGg4SBgn5/fHx6enp4enh8eX58gX+EgYWEhoWFhYOEgYN+gXuAen56fXt9fX1/foJ/hICEgIR/g36Bfn99fn18fnyAfIF9g3+EgYSChIOCg4CCfoF8gHp+eX15fHp8fH1/f4KAhIKGg4aDhYODgoCAfn58fXt9en17fX1/f4CBgoODhIOEg4OCgoCAfn59fHx7e3p8e318f32BgIKCg4SEhYSGg4WCg4CBfX58fHp7enp7e318f32Bf4OAhIGEgYOCgoKAgn6CfIJ8gnyBfYB+f39+gXyCfIJ7gnuCfIB9f35+gH2CfIN9hH6Ff4SBhIKCg4GDf4F9gHx+e317fHt9fH5+f3+AgYGCgoOCg4KDgYKAgX5/fX58fnt+fH59f3+AgoCEgYWAhYCEf4J/gH59fnp+eX54f3l/e4B+gYGBhIKHgoeCh4GFgYKAfn97fnh+eH14fXp9fX2AfoN/hYCGgYaChYKDgoCCfYJ7gXqBeoB7gH1/f36BfYN9g3yDfIJ8gX2Afn6AfoF9g32EfoV/hYCEgYKBgIF+gXyAe396fnp+fH59fn9/gYGDgoODg4OCgoGBf39+fX58fnt+fH99gH+BgYGDgoWChoGFgIR/gX5/fHx7enx5fXp+e4B9gn+DgoOEg4aDhoKFgYOAgH9+fnx9enx6fHt9fH1/foF/g3+FgIWBhIGDgoGCfoJ8gnuCeoJ7gXyAfn6AfYJ8hHuEe4N7gn2Afn+AfYJ8g3yEfYR+g3+CgIGBf4F+gX2BfIB8f31+fn5/foB+gX+BgYGCgYKAgn+Bf39+fn58fnx/fH99gH6BgIGCgoOChIGEgYOAgn+Afn58fHx7fHt8e318f36BgIOChISFhYWEhIOCgYF/f359fHx8e3x7fXt+fIB+gX+CgIOBgoKBgn+DfYJ8gnuCe4F8gX2Af3+CfoR9hnyHe4d7hnyEfYJ+f4B8gXqDeYR4hHqEfIN+goGAg36FfIZ7hnuEe4J8f358f3qBeYJ4g3iDeYJ6gXyAfn6AfoJ9hX2Hfol/ioCKgImBhoKCgn6BeYB2f3J+cX1wfHF8c313fnt/gYGFgomDjISNhI2Di4KIgIR+gHx8e3l7d3t2fHd+eH96gHyBfoKAgoGCg4KEgoWBhoCHgIh/iH6HfoZ+g32AfX1+en54fnd/dn93gHiBeoJ8goCCg4KHgomBi3+Mfot9iXyGfIJ8fn16fneAdoF2gnaDeIN6gnyBfn+AfoJ+hH6Gfod/iICIgIiBh4GFgoOBf4B7f3h+dX1zfHN8dH13fnt/f4GDgoeDioSLg4uDioGIgIV+gn1+fHt8eXx3fHZ9d354f3qAe4F9gn+CgIKCgYOBhICGgIZ/h3+Hf4Z/hH+Cf39+e354fnZ+dX51f3aAeIF7gn6DgoOFgoiBiYCJfol9h32FfIJ9f359f3uAeYJ5gniDeIN5gXmAen58fX18gHyCfYV+h4CJgYqCioOIg4WCgYF9gHl+dX1zfHJ8c3x1fXl+fYCBgYWCiIOKg4uDioKJgYeAg36AfX18enx4fHd9d354gHmBe4F9gn+BgYGCgIOAhICEgIWAhYCFgIZ/hX+Ef4J+gH59fXp9eH12fnZ/doF4gnuCfoOCg4WCiIGJgIp+iX2He4R7gnx/fX1/e4F6gnmDeIN5gnmBeoB8f35/gH6CfoR/hn+HgIiAiICIgYaBhIGBgX2Aen93fnV9dH10fXZ+eX99gIGBhYKIgoqDi4KKgoiBhYCCf39+fH15fHh8eH14fnl/e4B9gX6CgIKBgoGCgoGCgYOAhH+FfoV+hX2FfYR9gn2Afn1+en93gHaAdYF2gnmCfIKAgoSCiIGKgIt/in6IfYZ8g3x/fHx9en54f3iBeIJ5gnuCfIJ+gX+AgH+BfoJ+g32EfoV+hn+HgIaBhYKDgYCBfX96fnd9dnx1fXZ9eH97gH+Bg4OGg4mEi4SLg4mCh4CDfn99fHt5e3d7d3t4fHp+fIB+goCDgYSBhIGEgIOAgYGAgX+CfoR9hX2FfYV+g36Bf35/e395f3d/d393gHiAe4F+goGChIKGgoiBiYCIf4d+hX2CfH98fX17fnl/eYB5gXqCe4J8gn2BfoB/gIF/gn+DfoV+hn+Gf4aAhYGEgYKBf4B8f3l+d312fXZ9d355f3yAgIGDgoaCiIOJg4mCiIGGgIN+gH19fHp8eXx4fXh+eYB7gX2Cf4KAgoGCgoGCgYKAgn+CfoN+g36EfoR/g4CCgICAfoB8f3p/eH93fnd+eX97f32AgYGEgoeCiYKKgYmAiH+FfoJ9f3x8fHp9eX14f3iAeYF7gXyBfoF/gYGBgoCDgIV/hX+Gfod+hn6Gf4R/gYB+gHt/eH92fnV+dX53fnp/fYCBgISBh4KJgomCiIGHgIV/gn6AfX18e3x6fHp9en57gHyCfYN9g36DfoJ+gYCAgX6DfYR9hn2Gfod/hn+EgIKAf4F8gHmAeIB3f3d/eH96f3yAf4CBgYSChoKHgYeBh4CGf4R+gn2AfX59fH57f3qAeoF6gnuCe4J8gn2Bf4CAf4J+hH6Gfod+h36Gf4WAg4GAgX2CeoF4gXeAd393fnl9e31+foB/g4CFgYeCh4KHg4aChYGCgIB/fn58fXp8en16fnt/fIB+gX+CgYKBgoKCgoGBgIB/f35/fX9+gH6Af4F/goCCgIKAgoCBf4B/fn99f3x/e4B7gHuAfIF+gICAgoCEf4V/hn6GfoV+g36Bfn5+e395gHiBd4F3gXiBeoF9gIB/g36Ffod9iH2Ifoh/hoCDgYCBfIF5gXeAdoB2f3d/en59foF+hH6Hf4iAiYGIgYaCg4KBgX6AfH96fnp9en17fX19f3+BgIOBhIKDgoOCgoKAgX+Af39/fn99gH2BfoJ/gn+DgIKAgoCBgICAf4B9f3x/e396fnp/e399f3+AgoCEgIeBiIGIgIiAhn+Df4B+fX56f3h/d393gHeAeYB8gH+AgoCFf4d/iH+If4d/hoCDgICAfYB7gHmAeIB4gHl/e399fn9+gX6Df4R/hYCFgISBg4KBgn+BfYF8gHt+e358fX19f32AfoF/goCBgICBf4J+gn2BfYF9gH1/fn+AfoF+g36EfoR+hH6Df4GAf4F9gnuBeYF4gHl/en58fn5+gH6Df4WAhoCHgYeBhoGEgIKAf399f3p+eH53fnd+eH95f3yAf4CCgYWBh4CJgImAiICGgIOAgIB8gHp/eH93f3d/eX57fn5+gX6Df4V/hYCFgIWBg4GBgX+BfoF9gH2AfX9+f39+gH6BfYF9gX2Afn9/foB9gXyCfIJ9gn6Bf4CBf4J+g36EfYV+hH6Df4J/gIB+gXyBeoF5gHl/eX96fnx+fn6AfoN/hICGgYaBhoKGgoWCg4GAgH5/fH55fXh9d313fnl+e39+gIGAhIGGgYiBiIGHgYaBg4GBgH5/e396fnl+eX56fnx+fn+Af4KAg4CEgYSBg4GCgYGAgIB/f35/fn9/f4B/gX+Bf4J/gX+Af39/fX98f3t/e4B7gHyBfoGAgYKAhICGf4d/h3+Gf4R/gn9/f31/eoB5gHiAeIB5gHuAfX9/f4J/hH+Ff4Z/h4CGgYWBhIGBgX+BfYB8gHp/en55fnp+e358fn5/gH+CgISBhYGGgoaBhYGDgIGAf399f3t+en56fnt/fH9+f39/gICBgIGAgYCAgICAf4B/gH+Af3+Af4B/gX+CfoJ+gn6Bf4B/f4B9gHuAeoB6gHqAfIB9f4B+gn6EfYZ+h36Hf4aAhICCgH+BfIF6gXiBeIB4f3l/e359foB+gn6FfoZ/h4CGgIWBhIGCgYCBfoB9f3x/e356fnp+e398f35/f4CBgIKBg4GEgISAhH+Df4J/gX+AgH6AfX98f3x/fH99f35/f3+Af4GAgYCCgYGBgIGAgX+Af39/f39+gH6AfoF+gn+Cf4KAgYGAgX6BfYF8gXuAe397f31+f36BfoN+hX+Gf4aAhYCDgYGAf4B9gHyAe4B6gHp/e398f31/f3+Bf4N/hH+FgIWAhICDgIKAgIB/f31/fH58fnt/e398f32AfoB/gYGBgoGDgYOAhH+Df4N+gn6Afn9/fn99f3x/fH99gH2AfoB/gICAgYCBgIKAgoCBf4B/gH5/fn5+fn5+f39/gH+BgIKAgoGBgYCBf4F9gXyAfIB8f3x/fX5/foF9g36EfoV/hYCEgYKBgYF/gX2Ae4B6f3p+en57fn1+f3+AgIKBg4GEgYSBhICDf4J/gX5/fn5+fX58fnt/e4B7gHyBfYF/gYCBgoGDgIOAhH+Ef4N/gn+Bf39/fn99f3x/fH98gH2AfoB/gIGAgoCDgYOBg4GCgICAf39+f31+fX59fn9+gH+Cf4N/hICDgYKBgIF/gX2BfIB7gHx/fH9+fn9+gX6DfoR/hH+EgIOAgoCAgH9/fn99f3x/fH98f32AfoCAgIGAgoCDgIN/g3+Df4J/gX+Af39/fn99fn1+fX99f32AfoB+gX+BgIGBgYKAgoCDf4N/gn6Bfn9+fn59fnx+fH98f32Af4GAgYKBg4GDgYOBgoCBgH9/fX98fnx+fH59fn5+gH+Bf4KAg4CDgYOBgoGAgX+BfYF8gHuAe398f31/f36BfoJ/g3+Ef4SAg4CCgICAf4B9gHyAe4B7gHuAfYB+gICAgoCDgISAhH+Df4J/gX+Af35/fn99f31/fX99f32AfoB/gYCBgYGCgYKBg4CDgIKAgX+Af39+fn59fnx+fH58f32AfoF/gYGBgoGDgYOBg4CCgIGAf39+f31+fH58fnx+fX5/f4B/goCDgISBg4GCgYGBf4F9gHyAe4B7f3t/fX9/foF+g36EfoV/hH+DgIKAgIB+gXyAe4B6gHuAfH9+f4B/gn+Df4V/hX+Ef4N/gX+Af35/fX98f3x/fIB9gH6Af4CAgIGAgoCCgIKAgoCCgIJ/gX+Af39/fn99f31/fX99f31/fn9/gICAgYGCgYOBg4GDgIKAgX9/f35+fH57fnt+fH99f39/gYCCgIOAhICEgIOAgYB/gH2Ae396f3t/fH9+f4B/gn+Df4R/hICDgIJ/gH9+f31/e396gHuAfIB9gH+AgYCDgISAhH+Ef4N/gn+Af39/fX98f3t/e4B7gHyAfoCAgIKAg4CEgISAg4CBgH+AfoB9f31/fn9/f4B/gYCBgICAf4B+gH2AfIB9gH6Af4CBf4J/hH+Ef4R/g3+Bf39/fX98gHuAfIB9gH+AgoCEgIV/hn+Ff4N/gX9/f31/e397gHuAfIB+gICAgYCCf4N/gn+Bf39/fX98f3uAe4B7gX2Bf4GBgIOAhH+Ff4R+gn6Afn1+e395gHiAeYF6gXyBf4GCgISAhX+Ff4R/g3+Af35/fH97gHuAe4B9gH6AgICBf4F/gn+Bf4B/f39/gH6AfoB/gICAgX+Cf4J/gn+Bf4B/fn99f3x/e398gH2AfoCAgIJ/hH+Ef4R/g3+Cf4B/fn99f3yAfIB9gH6AgH+Bf4J/g3+Cf4F/gH9/f31/fX99gH2Af4CBgIKAhICEgIR/g3+Cf4B+fn58f3t/en96gHyAfoGAgYKBhICFgIZ/hX6DfoF+f359f3x/fIB8gH2Bf4GAgYGAgoCCf4F/gH9/f39/fn9/f39/gICBgIKAg4CCgIKAgIB/f31/fH97f3uAfIB+gICAgoCEf4V/hX+Ef4J/gH9+f3x/fIB8gHyAfoF/gYGAgoCDf4N/gn6Bfn9+fn99f32AfYB+gYCBgYGDgIOAhH+Df4J+gH5+fnx/e396gHuAfIB+gIGAg4CEf4V/hH+Df4J/gH9+f32AfIB8gH2BfoF/gICAgYCBf4F/gH6Afn9+fn5+fn5/f4CAgIGBgoGCgYKBgoCBf39/fn59fnx+fH58f31/f4CAgIKAgoCCgIKAgoCBgIB/f39+f31/fX9+gH+AgICBgIGAgX+Bf4B+f359fn1/fH99f36AgICBgYOBhIGEgIOAgn+Af35/fH97f3t/fIB9gH6AgICCgIOAg3+Df4N/gn6Af39/fYB9gHyBfYF+gX+BgICBgIJ/gX+BfoB+fn59f31/fYB/gICBgYGDgYOBg4CCf4F/f35+fnx+e397gHyAfoB/gYGAgoCDgIN/g3+CfoB+f35+fn1/fX9+gH+AgIGAgYGBgYCBgIB/gH9/fn5+fX59fn5/f3+Af4GAgoCDgIOAgn+Bf4B/fn99f3yAe4B8gH2AfoCAgIF/gn+Df4N+gn6Bfn9/fn9+gH2AfoF/gX+BgIGBgIGAgX+Afn9+fn5+fn1/fX9+gH+AgIGCgYOBg4CDgIJ/gX9/f35/fH97f3uAfIB9gH+AgYCCgIOAg3+Df4J/gX9/f35/fX99gH2AfoB/gYCAgYGBgIGAgYCAf39/f39+f35/fn9/f4CAgYCCgIKAgoCBgIF/f39+f31/fIB8gH2AfoB/gICAgn+Cf4N/gn+Bf4B/f39+f32AfoB+gH+AgICBgIGAgYCBf4B/f399f31/fH99f35/f4CBgIKAg4GDgIOAgn+Af39/fX98f3t/e398f32Af4CBgIKAg4CDgIOAgoCBf39/fn59fnx+fX99f39/gICCgIKBgoGCgYCBf4B+gH1/fX99f35+f3+Bf4J/g3+Df4OAgoCAgH+AfYB8gHyAfIB9f39/gH+Bf4N/g3+Cf4F/gH9/f36AfoB+gH6Af4CAgIGAgYCBf4B/f39+fn1+fX58f31/foCAgIKBg4GEgYSBhICCf4B/fn58fnt+en56f3uAfoCAgYKBhIGFgYWAhICDf4B+fn58fXt+e358f35/f4CBgYKBg4GDgYKBgYB/f35/fX58fn1+fX9/f4CAgoCDgIOAg4CCgIGAf4B9gHx/e398f32Af3+AgIGAgoCDgIKAgYCAgH+AfoB9gH2AfoB/gICAgICBgIGAgH9/f35/fX59f31/fn9/gICAgoGDgYOBhICCgIF/f359fnt+en56fnt/fYB/gIGBg4GEgoWBhIGDgIF/f39+fnx+fH58fn1/foCAgIKBgoGDgYKAgYCAf35/fX98f3x/fX9+f4B/gX+DgIOAhICDgIKAgYB/gH2AfIB8f3x/fX9+f39/gX+Cf4J/gn+Cf4GAgICAgH+AfoB+gH9/f3+Af4B/gH9/f39/fn9+f36AfoB/gICAgYCCgIKAg4CCgIF/gH9/fn5+fH58f3x/fIB+gH+AgYCCgYOAhICDgIN/gX+Af35/fX58f3x/fX9+gICAgYGCgYOBg4CCgICAf399f3x/fH98f31/f3+Bf4KAhICEgYSBg4GBgH+AfX98f3t+e358fn1/f3+AgIGAgoCCgYKBgYGBgICAf4B+f35/f35/foB/gH+Af39/f4B+gH6AfoB+gH6Af4CAf4F/gn+Df4N/gn+Bf4B/fn99f3yAe4B8gHyAfoCAgIGAg4CDgIOAgn+Bf4B/fn99f31/fX9+f39/gICBgIKBgoGCgIGAgIB+f31/fH98fnx+fn5/f4GAg4CEgYSBhIGDgYGBf4B9f3x/e357fnx+fX5/f4B/goCDgYOBg4GCgYGBgIB/f35/fn5+fn9+f39/f3+Af4B/gH+AfoB+gH6Af39/f4B/gX+Cf4N/g4CCgIGAgIB+gH2AfH97f3x/fH9+f4B/gX+CgIOAg4CCgIGAgIB+f31/fX59fn5/f3+AgIGAgYGCgYGBgIB/gH5/fX59fn1+fX5+foB/gn+DgISBhIGDgYKBgIF+gH1/fH57fnt9fH5+fn9/gYCCgIOBg4GDgYKBgYGAgH9/f35/fn5+f35/fn9/f4B/gH+BfoF+gX6Bf4B/f4B/gX+CfoJ/g3+Cf4F/gIB/gH6AfIB8gHyAfH99f39/gH+Bf4KAg4CDgIKAgX+Af35/fn99f31/fn9/f4CAgYCBgIKBgYGAgH+Afn99f3x+fH59fn5+gH+CgIOAhIGEgYOBgoGAgX6AfH97fnt+e318fX5+f3+BgIKBg4GDgoOCgoGBgIB/f39/fn59fn1+fn5+f39/gH+Bf4F/gn+Cf4F/gYCAgX+BfoJ9gn2CfYF+gH5/f36AfoF9gX2CfYF+gX+AgICBf4J/gn6CfoF+gX6Afn9/fn9+gH6AfoB/gYCBgYGCgYKAgoCBf4B/f35+fn1+fX59fn5+f3+BgIKBg4GDgoOCgoGBgH+Afn98fnx9e318fX1+fn+AgIGBgoGDgoKCgoKBgYCAf39+fn59fn1/fX9+f39/gH+Bf4F/gn+CfoJ+gX+Af3+AfoF9gX2CfYJ+gX+Bf4CAf4F+gn2CfYF9gX6Afn9/f4B+gX6BfoF+gX+Af39/f4B+gH6Bf4F/gYCAgYCBgIGAgX+Af39/fn99f31/fX99f35/f3+Bf4KAg4CDgYOBg4GBgICAfoB9f3x+fH58fn1+fn5/f4GAgoCDgYOBg4GCgYGBgIB/f35/fn5+fX59fn5/fn9/gICAgYCBgIF/gX+Bf4B/f4B+gH6BfoF+gX6Bf4B/gIB/gH6BfoF9gX6BfoB/f4B/gH+BfoF+gX6BfoB/f39/f36AfoB/gX+BgIGAgIGAgYCBf4B/f39+fn1/fX99f31/fn9/gIGAgoCCgYOBg4GCgIGAgH9+f31/fH58fnx+fX5+f39/gICBgIKBgoGCgYGBgIGAgH9/fn9+fn5+fn5/fn9+f39/gH+Bf4F/gn+CgIGAgIB/gH6AfoB+gH6AfoB/gH+AgH+Af4F/gX6Bf4F/gH9/gH+AfoB+gH6AfoB/gH9/gH+Af4F/gX+BgICAgIF/gX+Bf4B+gH5/fn5/fn9+f36AfoB/gICAgYCBgIKAgoCCf4F/gX+Af35/fn99f31/fX9+f39/gICAgIGAgYGBgYGAgYCAgICAf39/f39+f35/fn9+gH+Af4CAf4B/gX+Bf4F/gX+AgICAf4B+gH6AfoB+gH+Af4CAf4B/gX+Bf4F/gX+Af4CAf4B+gH6AfoB+gH9/f3+Af4B/gX+BgIGAgICAgH+Af4B/gH5/fn9/fn9+f36AfoB/gH+AgICBgIGAgoCCgIF/gH9/f39/fn59f31/fn9+f39/gICAgIGBgYGBgYGBgYCAgIB/f39/fn9+f35/fn9+f39/gH+AgIGAgYCBgIF/gX+Af39/f4B+gH6AfoB+f39/f3+Af4B/gX+Bf4GAgYCAgICAf4B/gH5/fn9+f39/f3+Af4B/gX+BgIGAgYCAgYCBf4F/gH6Afn9+f35+f35/foB+gX+BgIGAgYGAgoCCgIF/gX+Afn9+fn5+f35/fn9+gH6Af4CAgICAgYCBgIGAgYCAgIB/gH9/f39/f35/fn9/f39/f4CAgICAgICBgIF/gX+Bf4B/f4B/gH6AfoB+gH6Af4B/f4B/gH+Bf4F/gX+AgICAf4B/gH6AfoB+gH9/f3+Af4B/gX+Bf4GAgICAgH+BfoF+gH6AfoB+f39/f36AfoB+gX+Bf4GAgYCBgYCBgIF/gX6AfoB+f35/fn5/fn9+gH+Af4GAgYCBgIGAgICAgICAgIB/gH9/f39+f35/f39/f39/f3+AgICAgYCBgIGAgX+Af4B/f39/gH6AfoB+gH+Af3+Af4B/gH+Bf4F/gH+AgH+Af4B/gH6AfoB/gH9/f3+Af4B/gX+Bf4F/gX+AgICAf4B/gH6AfoB+gH9/f3+Af4B/gH+Bf4GAgYCAgICBgIF/gH+Af4B/f35/fn5/fn9+f39/f4CAgICAgYCBgIGAgICAgICAf39/f39/f39/fn9+f36Af4B/gH+AgICAgICAgICAgIB/gH+Af39/f4B/gH6Af4B/f39/gH+Af4B/gH+Af4CAf4B/gH+Bf4F/gX+Af4CAf4B/gH6AfoB+gH+Af3+Af4F/gX6BfoF+gH+Af3+Af4B+gH6BfoF/gICAgICBgIF/gX+Bf4B/f39+f35/fn9+f35/f4CAgICAgYCBgIGAgYCAgICAf4B+f35/fn9+fn5+f35/f4B/gH+BgIGAgIGAgYCBf4F/gH+Af4B/f39/gH+Af4B/gH+Af4CAf4B/gH+Af4B/f4B/gH+Af4B/gICAgICAf4B/gH+AfoB/gH9/gH+Af4F/gX+Bf4F/gH+Af3+Af4B+gH6AfoB/gH+AgICBgIF/gX+Bf4F/gH9/f39/fn9+f35/foB/gH+AgICBgIGAgYCBgIGAgIB/f35/fn9+f35/fn9/f4B/gH+Bf4GAgYCBgICAgIB/gH+Afn9+f35/f39/f4B/gH+Af4B/gH9/f3+Af4B/gH+Af4CAf4B/gH+AgICAgIB/gH+AfoB+gH9/f39/f4B/gH+Bf4F/gX+Af4CAf4B/gH6AfoB+gH+Af4CAgICAgX+Bf4F/gH+Af39/fn9+f35/foB/gH+AgICBgIGAgYCBgIGAgH9/f39/fn9+f35/f39/f4CAgICBgIGAgYCBgICAgIB/gH9/f39/f39/f39/gICAgICAgICAgICAgH9/f39/f39/f3+Af4CAgICBgIGAgICAgH+Af4B+gH5/fn9/f39/gH+Af4B/gX+Af4CAgIB/gH+AfoB+gH+Af4CAgIB/gH+Bf4B/gH+Af39/f39+f35/fn9/gH+AgICAgICAgYCBgIGAgICAf39/f39+f35/fn9/f39/f3+AgICAgYCBgICAgICAgH9/f39+f35/f39/f39/gH+AgIGAgYCBgICAgIB/gH9/f39/f39/f3+Af4CAgICAgICAgICAgH+Af39/f39/f39/f4B/gH+Af4GAgICAgICAf4B/gH+Af39/f39/gH+Af4F/gX+Bf4GAgIB/gH+AfoB+gH5/fn9/f4B/gH+BgIGAgYCBgICAgH9/f39/fn9+f35/fn9/f3+AgICAgICAgYCAgICAgH9/f39/f39/f39/f3+AgICAgICAgICAf4B/gH9/f39/f39/gH+Af4CAgICAgICAgIB/gH+Af4B/f39/f39/f39/gH+Af4B/gICAgICAgIB/gH+Af4B/f39/f3+Af4B/gH+Af4CAgICAgH+Af4B+gH5/fn9/f39/gH+Af4CAgYCBgICAgICAf39/f39/f39/f39/f39/gICAgICAgICAgICAgH+Af39/f39/f4B/gICAgICAgICAgICAf4B/f39/f39/f39/f3+Af4CAgICAgICAgICAgICAf39/f39/f39/f39/f3+Af4B/gICAgICAgIB/gH+Af4B/gH+Af4B/f4B/gH+Af4B/gH+Af4B/f39/f39/f39/f39/f39/gICAgICAgYCBgICAgICAgH9/f39/f35/fn9+f39/f3+AgICAgICAgICAgICAf4B/f39/f39/f4B/gH+Af4CAgIB/gH+Af39/f39/f39/f39/f4CAgICAgICAgICAgICAgH9/f39/f39+f39/f39/gICAgICAgICAgICAf4B/gH9/f39/f39/f3+Af4B/gH+Af4B/gICAf4B/f39/f39/f39/f3+Af4CAgICAgICAgICAgICAf4B/f39/fn9+f39/f39/f4CAgICAgICAgICAgICAgH9/f39/f39/f39/f4B/gH+Af4CAgH+Af39/f39/f39/f4B/gH+AgICAgICAgICAgIB/gH9/f39/f39/f39/f39/f4CAgICAgICAgICAgH+Af4B/f39/f39/f39/gH+Af4GAgYCAgICAgIB/gH9/fn9+f35/f39/gICAgICBgIGAgYCBgIB/f39/f39/fn9+f39/f39/gICAgICAgICAgICAgICAf39/f39/f39/f39/gH+Af4B/gH+Af4B/gH9/f39/f4B/gH+Af4CAgICAgICAgIB/gH+Af39/f39/f39/f39/f4CAgICAgICAgICAgH+Af4B/f39/f39/f39/gH+Af4CAgYCBgIB/gH9/f39/f39+f35/f4B/gH+AgICAgIGAgYCBgIB/gH9/f39+fn5+fn5/f39/f3+AgICAgIGBgYGAgICAgIB/f39/fn9+f39/f39/f4B/gICAgICAgH+Af4B/f39/f3+Af4B/gH+Af4B/gICAgICAf4B/gH+Af4B/gH+Af4B/gICAgICAgICAgICAgIB/gH9/f39/f39/f3+Af4B/gH+Bf4F/gH+Af4B/f39/f39/f39/gH+Af4CAgICAgICAgICAgH+Af39/f35/fn9/f39/f3+AgICAgICAgIGAgICAgIB/gH9/f39/f39/f39/f4B/gH+Af4B/gH+Af4B/gIB/gH+Af4B/gH+Af4B/gICAgICAgIB/gH+Af4B+f39/f39/f39/gH+AgICAgICAgIB/gH+Af4B/f39/f39/f4B/gH+Af4B/gH+Af4B/gH9/f3+Af4B/gH+Af4B/gH+AgICAgICAgICAf4B/gH9/fn9+f35/f39/f39/gICAgIGAgYCBgICAgH+Af39/f39/f39/f39/gH+Af4B/gICAgICAgIB/gH+Af4B/gH+Af4B/gH+Af4CAgIB/gH+Af4B/gH+Af4B/gH9/gH+Af4B/gH+Af4B/gH+AgICAf4B/gH+Af4B/gH+Af4B/gH+Af4B/f39/f39/f39/gH+Af4B/gH+AgICAgICAgICAf4B/gH9/f39/f39/f39/f39/f3+AgICAgICAgIGAgICAgIB/gH9/f39/f39/f39/f4B/gH+Af4CAgICAgICAgIB/gH+Af4B/gH+Af4B/f4B/gH+Af4B/gH+Af4B/f39/f39/f4B/gICAgICAgICAgICAgICAf39/f39/f39/f39/gH+Af4B/gH+Af4B/gH9/gH+Af4B/gH+Af4B/gH+AgICAgICAgH+Af4B/f35/fn9+f39/f39/gICAgICBgIGAgYCBgIB/gH+Af39/f39/f39/f39/f3+Af4B/gICAgICAgICAgH+Af4B/gH+Af4B/gH9/f3+Af4B/gH+Af4B/gH+Af39/f39/gH+Af4B/gICAgICAgICAgICAgH+Af39/f39/f39/f39/gH+Af4B/gH+Af4B/gH9/gH+Af4B/gH+Af4B/gICAgICAf4B/gH+Af4B+f35/fn9/f39/gH+AgIGAgYCBgIGAgICAgH9/f39/f35/fn9+f39/f4B/gICAgICAgICAgICAf4B/gH+Af4B/f39/f39/f4B/gH+Af4B/gH+Af4B/f39/f39/f4B/gH+Af4CAgICAgICAgICAgH9/f39/f39/f39/f3+Af4B/gH+Af4B/gICAgH+Af4B/gH+Af4B/gH+AgICAgIB/gH+Af4B/gH+Af39/f39/f3+Af4B/gICBgIGAgYCAgICAf39/f39/f39+f39/f39/gH+AgICAgICAgICAgICAgH+Af39/f39/f39/f39/gH+Af4B/gH+Af4B/gH+Af39/f39/f3+Af4B/gICAgICAgICAgICAf39/f39/f39/f39/f39/gH+Af4B/gH+AgICAf4B/gH+Af4B/gH+Af4B/gIB/gH+Af4B/gH+Af4B/f39/f3+Af4B/gH+Af4GAgICAgICAgIB/gH9/f39/f39/f39/f3+Af4CAgICAgICAgICAgH+Af4B/gH+Af4B/gH+Af39/f4B/gH+Af4B/gH+Af4B/f39/f3+Af4B/gH+Af4CAgICAgICAgICAf39/f39/f39/f39/f3+Af4B/gH+AgICAgIA="

def get_engine(hass, config, discovery_info=None):
    """Set up Pico speech component."""
    return NoTTSProvider(hass, config[CONF_LANG], config[CONF_BEEP])


class NoTTSProvider(Provider):
    """The No TTS API provider."""

    def __init__(self, hass, lang, beep):
        """Initialize No TTS provider."""
        self._hass = hass
        self._lang = lang
        self._beep = beep
        self.name = "No TTS"

    @property
    def default_language(self):
        """Return the default fake language."""
        return DEFAULT_LANG

    @property
    def supported_languages(self):
        """Return list of fake supported as languages."""
        return SUPPORTED_LANGUAGES

    async def async_get_tts_audio(self, message, language, options=None):
        """Load No TTS beep or no beep wav."""

        """Check beep activation"""
        if self._beep == "1":
            data = base64.b64decode(BEEP)
            
        return (None, None)
