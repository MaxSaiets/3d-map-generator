import type { Metadata } from "next";
import { Link } from "@/i18n/navigation";
import { pageMetadata } from "@/i18n/metadata";
import { getLegalDoc } from "@/lib/legal/content";
import { LegalArticle } from "@/components/LegalArticle";

export async function generateMetadata({ params }: { params: { locale: string } }): Promise<Metadata> {
  return pageMetadata({ locale: params.locale, path: "/privacy", ns: "privacyMeta" });
}

export default function PrivacyPage({ params }: { params: { locale: string } }) {
  const doc = getLegalDoc(params.locale, "privacy");
  return (
    <div className="mx-auto max-w-[760px] px-5 py-12 lg:px-8">
      <Link href="/" className="text-[13px] font-semibold text-ink-2 hover:text-ink">← monadruk</Link>
      <LegalArticle doc={doc} locale={params.locale} path="/privacy" />
    </div>
  );
}
