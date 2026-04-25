import { Link } from 'react-router-dom'

export default function Landing() {
  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-extrabold mb-4">
          Bars<span className="text-[#F97316]"> AI</span>
        </h1>
        <p className="text-white/40 mb-6">Landing page coming soon</p>
        <Link
          to="/register"
          className="inline-block bg-[#F97316] text-black font-bold px-6 py-3 rounded-xl"
        >
          Начать бесплатно
        </Link>
      </div>
    </div>
  )
}
