import { motion } from 'framer-motion'
import { FileText, Link2, Download, ExternalLink, File, Image, Video, Music } from 'lucide-react'
import type { StepResources } from '@/services/courseApi'

const FILE_ICONS: Record<string, typeof FileText> = {
  pdf: FileText,
  doc: FileText,
  docx: FileText,
  xls: FileText,
  xlsx: FileText,
  ppt: FileText,
  pptx: FileText,
  txt: FileText,
  csv: FileText,
  png: Image,
  jpg: Image,
  jpeg: Image,
  gif: Image,
  svg: Image,
  webp: Image,
  mp4: Video,
  webm: Video,
  mp3: Music,
  wav: Music,
  ogg: Music,
}

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

interface Props {
  step: StepResources
  onComplete: () => void
}

export function ResourcesStep({ step, onComplete }: Props) {
  return (
    <div className="space-y-4">
      {step.title && (
        <h3 className="text-lg font-bold text-white">{step.title}</h3>
      )}
      {step.description && (
        <p className="text-sm text-white/60">{step.description}</p>
      )}

      <div className="space-y-2">
        {step.items.map((item, i) => {
          const ItemIcon = item.type === 'file' && item.fileType
            ? (FILE_ICONS[item.fileType] || File)
            : Link2

          return (
            <motion.a
              key={i}
              href={item.url}
              target="_blank"
              rel="noopener noreferrer"
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.05 }}
              className="flex items-center gap-3 p-3 rounded-xl bg-white/[0.03] border border-white/6 hover:border-[#F97316]/30 hover:bg-white/[0.05] transition-all group"
            >
              <div className="w-10 h-10 rounded-xl bg-[#F97316]/10 flex items-center justify-center shrink-0">
                <ItemIcon size={18} className="text-[#F97316]" />
              </div>

              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-white truncate">{item.label}</p>
                <div className="flex items-center gap-2 mt-0.5">
                  {item.fileType && (
                    <span className="text-[10px] text-white/30 uppercase">{item.fileType}</span>
                  )}
                  {item.fileSize && (
                    <span className="text-[10px] text-white/30">{formatSize(item.fileSize)}</span>
                  )}
                  {item.type === 'link' && (
                    <span className="text-[10px] text-white/30 truncate">{item.url}</span>
                  )}
                </div>
              </div>

              <div className="shrink-0 text-white/20 group-hover:text-[#F97316] transition-colors">
                {item.type === 'file' ? <Download size={16} /> : <ExternalLink size={16} />}
              </div>
            </motion.a>
          )
        })}
      </div>

      <div className="flex justify-center pt-4">
        <button
          onClick={onComplete}
          className="px-6 py-2.5 rounded-xl font-semibold text-sm text-white transition-opacity"
          style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
        >
          Продолжить
        </button>
      </div>
    </div>
  )
}
