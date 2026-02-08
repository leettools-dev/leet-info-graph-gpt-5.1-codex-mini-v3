import { createI18n } from 'vue-i18n'

import en from './en/common'
import ja from './ja/common'
import zh from './zh/common'

const messages = {
  en,
  ja,
  zh,
}

const i18n = createI18n({
  legacy: false,
  locale: 'en',
  messages,
})

export default i18n
