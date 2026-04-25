import { useEffect, useRef } from 'react'

export function StarField() {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    if (!ctx) return

    let animationId: number
    let width = window.innerWidth
    let height = document.body.scrollHeight

    canvas.width = width
    canvas.height = height

    // Generate stars
    const stars = Array.from({ length: 200 }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      size: Math.random() * 1.5 + 0.5,
      opacity: Math.random() * 0.7 + 0.3,
      twinkleSpeed: Math.random() * 0.02 + 0.005,
      twinkleOffset: Math.random() * Math.PI * 2,
    }))

    // Generate comets
    const comets: Array<{
      x: number
      y: number
      length: number
      speed: number
      opacity: number
      angle: number
      active: boolean
      life: number
    }> = []

    const spawnComet = () => {
      comets.push({
        x: Math.random() * width * 0.8,
        y: -20,
        length: Math.random() * 80 + 60,
        speed: Math.random() * 3 + 2,
        opacity: Math.random() * 0.5 + 0.3,
        angle: Math.PI / 4 + (Math.random() - 0.5) * 0.3,
        active: true,
        life: 0,
      })
    }

    let time = 0

    const draw = () => {
      ctx.clearRect(0, 0, width, height)

      // Draw stars with twinkling
      stars.forEach((star) => {
        const twinkle = Math.sin(time * star.twinkleSpeed + star.twinkleOffset) * 0.5 + 0.5
        const alpha = star.opacity * (0.4 + twinkle * 0.6)
        ctx.beginPath()
        ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2)
        ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`
        ctx.fill()
      })

      // Draw comets
      comets.forEach((comet) => {
        if (!comet.active) return

        comet.x += Math.cos(comet.angle) * comet.speed
        comet.y += Math.sin(comet.angle) * comet.speed
        comet.life++

        if (comet.y > height + 50 || comet.x > width + 50) {
          comet.active = false
          return
        }

        const fadeIn = Math.min(comet.life / 20, 1)
        const gradient = ctx.createLinearGradient(
          comet.x,
          comet.y,
          comet.x - Math.cos(comet.angle) * comet.length,
          comet.y - Math.sin(comet.angle) * comet.length
        )
        gradient.addColorStop(0, `rgba(249, 115, 22, ${comet.opacity * fadeIn})`)
        gradient.addColorStop(0.3, `rgba(251, 191, 36, ${comet.opacity * 0.5 * fadeIn})`)
        gradient.addColorStop(1, 'rgba(251, 191, 36, 0)')

        ctx.beginPath()
        ctx.moveTo(comet.x, comet.y)
        ctx.lineTo(
          comet.x - Math.cos(comet.angle) * comet.length,
          comet.y - Math.sin(comet.angle) * comet.length
        )
        ctx.strokeStyle = gradient
        ctx.lineWidth = 1.5
        ctx.stroke()

        // Comet head glow
        ctx.beginPath()
        ctx.arc(comet.x, comet.y, 2, 0, Math.PI * 2)
        ctx.fillStyle = `rgba(255, 255, 255, ${comet.opacity * fadeIn})`
        ctx.fill()
      })

      time++

      // Spawn comets occasionally
      if (Math.random() < 0.005) {
        spawnComet()
      }

      // Cleanup inactive comets
      if (comets.length > 10) {
        const activeComets = comets.filter((c) => c.active)
        comets.length = 0
        comets.push(...activeComets)
      }

      animationId = requestAnimationFrame(draw)
    }

    draw()

    const handleResize = () => {
      width = window.innerWidth
      height = document.body.scrollHeight
      canvas.width = width
      canvas.height = height
    }

    window.addEventListener('resize', handleResize)

    return () => {
      cancelAnimationFrame(animationId)
      window.removeEventListener('resize', handleResize)
    }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      className="fixed inset-0 pointer-events-none z-0"
      style={{ opacity: 0.8 }}
    />
  )
}
