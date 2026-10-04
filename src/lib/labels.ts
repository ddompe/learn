import en from '../i18n/en.json';
import es from '../i18n/es.json';

const all: Record<string, typeof en> = { en, es };

export function getLabels(locale: string | undefined): typeof en {
	return all[locale ?? 'en'] ?? en;
}
