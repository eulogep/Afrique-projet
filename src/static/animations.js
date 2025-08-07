// ===== ANIMATIONS ET EFFETS INTERACTIFS INSPIRÉS DE UIVERSE.IO =====

// ===== GESTIONNAIRE D'ANIMATIONS =====
class AnimationManager {
    constructor() {
        this.observers = [];
        this.particles = [];
        this.init();
    }

    init() {
        this.setupIntersectionObserver();
        this.createParticles();
        this.setupRippleEffects();
        this.setupProgressBars();
        this.setupCircleProgress();
        this.setupGlitchEffects();
    }

    // ===== OBSERVATEUR D'INTERSECTION POUR LES ANIMATIONS D'ENTRÉE =====
    setupIntersectionObserver() {
        const options = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    observer.unobserve(entry.target);
                }
            });
        }, options);

        // Observer tous les éléments avec des classes d'animation
        document.querySelectorAll('.slide-up, .slide-left, .slide-right, .zoom-in').forEach(el => {
            observer.observe(el);
        });
    }

    // ===== SYSTÈME DE PARTICULES =====
    createParticles() {
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles';
        document.body.appendChild(particlesContainer);

        for (let i = 0; i < 50; i++) {
            this.createParticle(particlesContainer);
        }
    }

    createParticle(container) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Position aléatoire
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 6 + 's';
        particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
        
        container.appendChild(particle);
        this.particles.push(particle);
    }

    // ===== EFFETS DE RIPPLE =====
    setupRippleEffects() {
        document.addEventListener('click', (e) => {
            const rippleButton = e.target.closest('.ripple-button');
            if (rippleButton) {
                this.createRipple(e, rippleButton);
            }
        });
    }

    createRipple(event, element) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple-effect');

        element.appendChild(ripple);

        setTimeout(() => {
            ripple.remove();
        }, 600);
    }

    // ===== BARRES DE PROGRESSION =====
    setupProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        progressBars.forEach(bar => {
            const fill = bar.querySelector('.progress-fill');
            if (fill) {
                const percentage = fill.getAttribute('data-percentage') || 0;
                setTimeout(() => {
                    fill.style.width = percentage + '%';
                }, 100);
            }
        });
    }

    // ===== CERCLES DE PROGRESSION =====
    setupCircleProgress() {
        const circles = document.querySelectorAll('.circle-progress');
        circles.forEach(circle => {
            const progress = circle.querySelector('.progress');
            if (progress) {
                const percentage = progress.getAttribute('data-percentage') || 0;
                const circumference = 283; // 2 * π * r (r = 45)
                const offset = circumference - (percentage / 100) * circumference;
                
                setTimeout(() => {
                    progress.style.strokeDashoffset = offset;
                }, 100);
            }
        });
    }

    // ===== EFFETS DE GLITCH =====
    setupGlitchEffects() {
        const glitchElements = document.querySelectorAll('.glitch-text');
        glitchElements.forEach(element => {
            element.setAttribute('data-text', element.textContent);
            
            element.addEventListener('mouseenter', () => {
                element.style.animation = 'glitch 0.3s infinite';
            });
            
            element.addEventListener('mouseleave', () => {
                element.style.animation = 'none';
            });
        });
    }

    // ===== ANIMATIONS DE CHARGEMENT =====
    showLoading(element, type = 'spinner') {
        const loadingElement = document.createElement('div');
        loadingElement.className = type === 'spinner' ? 'loading-spinner' : 'pulse-spinner';
        
        element.appendChild(loadingElement);
        element.classList.add('loading');
        
        return loadingElement;
    }

    hideLoading(element) {
        const loadingElement = element.querySelector('.loading-spinner, .pulse-spinner');
        if (loadingElement) {
            loadingElement.remove();
        }
        element.classList.remove('loading');
    }

    // ===== ANIMATIONS DE TRANSITION =====
    animateElement(element, animation, duration = 600) {
        element.style.animation = `${animation} ${duration}ms ease-out`;
        
        return new Promise(resolve => {
            setTimeout(() => {
                element.style.animation = '';
                resolve();
            }, duration);
        });
    }

    // ===== EFFETS DE PARALLAXE =====
    setupParallax() {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallaxElements = document.querySelectorAll('.parallax');
            
            parallaxElements.forEach(element => {
                const speed = element.getAttribute('data-speed') || 0.5;
                const yPos = -(scrolled * speed);
                element.style.transform = `translateY(${yPos}px)`;
            });
        });
    }

    // ===== EFFETS DE TYPING =====
    typeWriter(element, text, speed = 100) {
        let i = 0;
        element.textContent = '';
        
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }

    // ===== EFFETS DE COUNTER =====
    animateCounter(element, target, duration = 2000) {
        const start = 0;
        const increment = target / (duration / 16);
        let current = start;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current).toLocaleString();
        }, 16);
    }

    // ===== EFFETS DE MORPHING =====
    setupMorphingButtons() {
        const morphButtons = document.querySelectorAll('.morph-button');
        morphButtons.forEach(button => {
            button.addEventListener('mouseenter', () => {
                button.style.transform = 'scale(1.05)';
            });
            
            button.addEventListener('mouseleave', () => {
                button.style.transform = 'scale(1)';
            });
        });
    }

    // ===== EFFETS DE FOCUS =====
    setupFocusEffects() {
        const focusElements = document.querySelectorAll('.focus-ring');
        focusElements.forEach(element => {
            element.addEventListener('focus', () => {
                element.classList.add('focused');
            });
            
            element.addEventListener('blur', () => {
                element.classList.remove('focused');
            });
        });
    }

    // ===== ANIMATIONS DE NAVIGATION =====
    setupNavigationAnimations() {
        const navItems = document.querySelectorAll('.modern-nav-item');
        const indicator = document.querySelector('.nav-indicator');
        
        if (indicator) {
            navItems.forEach(item => {
                item.addEventListener('mouseenter', () => {
                    const rect = item.getBoundingClientRect();
                    indicator.style.left = rect.left + 'px';
                    indicator.style.width = rect.width + 'px';
                });
            });
        }
    }

    // ===== EFFETS DE SCROLL =====
    setupScrollEffects() {
        let ticking = false;
        
        function updateScrollEffects() {
            const scrolled = window.pageYOffset;
            const elements = document.querySelectorAll('.scroll-effect');
            
            elements.forEach(element => {
                const speed = element.getAttribute('data-scroll-speed') || 1;
                const yPos = scrolled * speed;
                element.style.transform = `translateY(${yPos}px)`;
            });
            
            ticking = false;
        }
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(updateScrollEffects);
                ticking = true;
            }
        });
    }

    // ===== EFFETS DE HOVER AVANCÉS =====
    setupAdvancedHoverEffects() {
        const hoverElements = document.querySelectorAll('.floating-card, .glass-card');
        
        hoverElements.forEach(element => {
            element.addEventListener('mouseenter', (e) => {
                const rect = element.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                element.style.setProperty('--mouse-x', x + 'px');
                element.style.setProperty('--mouse-y', y + 'px');
            });
        });
    }

    // ===== UTILITAIRES =====
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
}

// ===== INITIALISATION =====
document.addEventListener('DOMContentLoaded', () => {
    window.animationManager = new AnimationManager();
    
    // Ajouter les classes d'animation aux éléments existants
    document.querySelectorAll('.modern-card').forEach((card, index) => {
        card.classList.add('floating-card', 'slide-up');
        card.style.animationDelay = (index * 0.1) + 's';
    });
    
    document.querySelectorAll('.modern-btn').forEach(btn => {
        btn.classList.add('ripple-button');
    });
    
    document.querySelectorAll('.modern-stat-card').forEach((stat, index) => {
        stat.classList.add('glass-card', 'zoom-in');
        stat.style.animationDelay = (index * 0.2) + 's';
    });
});

// ===== EXPORT POUR UTILISATION GLOBALE =====
window.AnimationManager = AnimationManager; 