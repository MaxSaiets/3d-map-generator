/**
 * Реальні фото надрукованих гір (зйомка власника, тло прибране й замінене студійним).
 * Серверний компонент: показується на /gory, /gory/[slug], /mountains, /karpaty.
 * 09.11.2026 — до цього на сторінках гір були лише рендери рельєфу, без жодного фото виробу.
 * Ціна гір індивідуальна; для uk показуємо орієнтир власника (біла ≈20×20 см ≈ 2000 ₴).
 */
import type { AppLocale } from "@/i18n/routing";

export const MOUNTAIN_PHOTOS = [
  "mountain-1",
  "mountain-2",
  "mountain-3",
  "mountain-4",
] as const;

type Copy = {
  h2: string;
  lead: string;
  captions: [string, string, string, string];
  price: string | null;
  cta: string;
  note: string;
};

const UK: Copy = {
  h2: "Так виглядають наші гори наживо",
  lead: "Реальні вироби з нашого принтера — не рендери. Рельєф друкується з висот супутника й лідара, тож кожен хребет і кулуар на своєму місці.",
  captions: [
    "Матергорн з ручним розписом акрилом: скелі, сніг, льодовики",
    "Матергорн у білому — чистий рельєф без фарби",
    "Піп Іван з прапорцем на вершині й гравіюванням на цоколі",
    "Розписана модель зблизька: видно кожен гребінь",
  ],
  price: "Біла модель ≈20×20 см — орієнтовно 2000 ₴. Розпис, прапорець на вершині, гравіювання дати сходження чи імен — за запитом.",
  cta: "Дізнатися ціну в Telegram",
  note: "Відповідаємо зазвичай протягом години. Доставка Новою Поштою по Україні.",
};

const EN: Copy = {
  h2: "What our mountains look like in real life",
  lead: "Real prints from our printer, not renders. The terrain comes from satellite and lidar elevation data, so every ridge and couloir is where it should be.",
  captions: [
    "Matterhorn hand-painted with acrylics: rock, snow, glaciers",
    "Matterhorn in plain white: pure terrain, no paint",
    "Pip Ivan with a summit flag and an engraved base",
    "Painted model up close: every ridge is visible",
  ],
  price: null,
  cta: "Ask about a print on Telegram",
  note: "Printed models are delivered within Ukraine. For other countries, write to us — we are open to partnerships.",
};

export default function RealMountainPrints({ locale, className = "" }: { locale: AppLocale; className?: string }) {
  const c = locale === "uk" ? UK : EN;
  return (
    <section className={`rounded-[22px] border border-line-soft bg-white/70 px-5 py-6 sm:px-7 ${className}`} aria-labelledby="real-mountains-h2">
      <h2 id="real-mountains-h2" className="text-[clamp(20px,2.4vw,26px)] font-semibold leading-tight text-ink">{c.h2}</h2>
      <p className="mt-2 max-w-[720px] text-[14.5px] leading-relaxed text-ink-2">{c.lead}</p>
      <ul className="mt-5 grid grid-cols-2 gap-3 lg:grid-cols-4">
        {MOUNTAIN_PHOTOS.map((img, i) => (
          <li key={img}>
            <figure className="overflow-hidden rounded-[16px] border border-line-soft bg-[#ece7de]">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={`/real/${img}.webp`}
                alt={c.captions[i]}
                width={1200}
                height={900}
                loading={i < 2 ? "eager" : "lazy"}
                className="aspect-[4/3] h-auto w-full object-cover"
              />
              <figcaption className="px-3 py-2 text-[12.5px] leading-snug text-ink-3">{c.captions[i]}</figcaption>
            </figure>
          </li>
        ))}
      </ul>
      {c.price && <p className="mt-5 text-[15px] font-semibold leading-relaxed text-ink">{c.price}</p>}
      <div className="mt-4 flex flex-wrap items-center gap-x-4 gap-y-2">
        <a
          href="https://t.me/monadruk"
          target="_blank"
          rel="noopener noreferrer"
          data-track="mountain_price_tg"
          className="inline-flex min-h-[48px] items-center justify-center rounded-[22px] bg-[var(--accent-strong)] px-6 py-3 text-sm font-semibold text-white transition hover:opacity-90"
        >
          {c.cta} →
        </a>
        <span className="text-[13px] leading-relaxed text-ink-3">{c.note}</span>
      </div>
    </section>
  );
}
