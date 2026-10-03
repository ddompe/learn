// Load i18n strings for a given locale and component
export function t(locale: string, component: string, key: string): string {
	const i18n: Record<
		string,
		Record<string, Record<string, string | Record<string, string>>>
	> = {
		en: {},
		es: {},
	};

	// Dynamically imported at build time
	return `${component}.${key}`;
}

// Get i18n strings for a component
export async function getI18nStrings(
	locale: string,
	component: string,
): Promise<Record<string, string>> {
	try {
		const module = await import(`../i18n/${locale}.json`);
		return module.default?.[component] || {};
	} catch {
		return {};
	}
}
